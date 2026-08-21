#!/usr/bin/env node

/**
 * CDPN Sync System — Bidirectional README ↔ Web synchronization
 * 
 * Usage:
 *   node sync.js pull    # GitHub READMEs → site/content/ (one-way)
 *   node sync.js push    # site/content/ → create GitHub PR (one-way)
 *   node sync.js status  # Show sync status
 *   node sync.js build   # Pull + VitePress build
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const ROOT = path.resolve(__dirname, '..');
const SITE_CONTENT = path.resolve(__dirname, 'content');
const GITHUB_REPO = 'https://github.com/0xvanguard/CyberDefense-Pro-Network';

// Mapping: GitHub path → site/content path
const SYNC_MAP = {
  // Module READMEs
  '01-CIBERSEGURIDAD/README.md': 'modules/red-team/index.md',
  '01-CIBERSEGURIDAD/01-reconocimiento-osint/README.md': 'modules/red-team/01-reconocimiento-osint.md',
  '01-CIBERSEGURIDAD/02-pentesting-red-team/README.md': 'modules/red-team/02-pentesting-red-team.md',
  '01-CIBERSEGURIDAD/03-analisis-vulnerabilidades/README.md': 'modules/red-team/03-analisis-vulnerabilidades.md',
  '01-CIBERSEGURIDAD/04-explotacion-web/README.md': 'modules/red-team/04-explotacion-web.md',
  '01-CIBERSEGURIDAD/05-post-explotacion/README.md': 'modules/red-team/05-post-explotacion.md',
  '01-CIBERSEGURIDAD/06-forense-digital/README.md': 'modules/red-team/06-forense-digital.md',
  '01-CIBERSEGURIDAD/07-ingenieria-social/README.md': 'modules/red-team/07-ingenieria-social.md',
  '01-CIBERSEGURIDAD/08-criptografia/README.md': 'modules/red-team/08-criptografia.md',
  
  // Blue Team
  '03-blue-team-defensa/README.md': 'modules/blue-team/index.md',
  
  // AI Agents
  '03-IA-AGENTES-HERRAMIENTAS/README.md': 'modules/ai-agents/index.md',
  '03-IA-AGENTES-HERRAMIENTAS/01-agentes-osint/README.md': 'modules/ai-agents/01-agentes-osint.md',
  '03-IA-AGENTES-HERRAMIENTAS/02-agentes-pentest/README.md': 'modules/ai-agents/02-agentes-pentest.md',
  '03-IA-AGENTES-HERRAMIENTAS/03-llm-security/README.md': 'modules/ai-agents/03-llm-security.md',
  '03-IA-AGENTES-HERRAMIENTAS/03-mlsecops-llm-security/README.md': 'modules/ai-agents/04-mlsecops.md',
  '03-IA-AGENTES-HERRAMIENTAS/05-automatizacion-python/README.md': 'modules/ai-agents/05-automatizacion-python.md',
  
  // Purple Team
  '04-purple-team-colaboracion/README.md': 'modules/purple-team/index.md',
  
  // Seguridad de la Información
  '02-SEGURIDAD-INFORMACION/README.md': 'modules/seguridad-informacion/index.md',
  
  // Fundamentos
  '00-FUNDAMENTOS/README.md': 'modules/fundamentos/index.md',
  
  // Labs (READMEs)
  'labs/intermedio/recon-01/README.md': 'labs/intermedio/recon-01.md',
  'labs/intermedio/pentest-01/README.md': 'labs/intermedio/pentest-01.md',
  'labs/intermedio/webapp-01/README.md': 'labs/intermedio/webapp-01.md',
  'labs/intermedio/privesc-01/README.md': 'labs/intermedio/privesc-01.md',
  'labs/intermedio/vulnscan-01/README.md': 'labs/intermedio/vulnscan-01.md',
  'labs/intermedio/web-01/README.md': 'labs/intermedio/web-01.md',
  'labs/intermedio/crypto-01/README.md': 'labs/intermedio/crypto-01.md',
  'labs/intermedio/disk-forensics-01/README.md': 'labs/intermedio/disk-forensics-01.md',
  'labs/avanzado/ad-01/README.md': 'labs/avanzado/ad-01.md',
  'labs/avanzado/malware-01/README.md': 'labs/avanzado/malware-01.md',
  'labs/avanzado/cloud-01/README.md': 'labs/avanzado/cloud-01.md',
  'labs/avanzado/forensics-01/README.md': 'labs/avanzado/forensics-01.md',
  'labs/avanzado/reverse-eng-01/README.md': 'labs/avanzado/reverse-eng-01.md',
  'labs/avanzado/net-forensics-01/README.md': 'labs/avanzado/net-forensics-01.md',
};

/**
 * Add VitePress frontmatter to markdown content
 */
function addFrontmatter(content, title, description) {
  // Don't add if already has frontmatter
  if (content.startsWith('---')) return content;
  
  // Quote titles with special YAML characters
  const safeTitle = title.includes(':') || title.includes('#') || title.includes('"') 
    ? `"${title.replace(/"/g, '\"')}"` 
    : title;
  const safeDesc = (description || title);
  const safeDescQuoted = safeDesc.includes(':') || safeDesc.includes('#') || safeDesc.includes('"')
    ? `"${safeDesc.replace(/"/g, '\"')}"`
    : safeDesc;
  
  const frontmatter = `---
title: ${safeTitle}
description: ${safeDescQuoted}
---

`;
  return frontmatter + content;
}

/**
 * Transform GitHub README links to VitePress-compatible paths
 */
function transformLinks(content, sourcePath) {
  // Convert relative links like ../other-module/ to VitePress paths
  // Convert GitHub raw links to internal links
  return content
    // Fix relative links to other READMEs
    .replace(/\]\(\.\.\/([\w-]+)\/README\.md\)/g, '](/modules/$1/)')
    .replace(/\]\(\.\/([\w-]+)\/README\.md\)/g, '](/modules/$1/)')
    // Fix image paths (keep as-is for now, they'll need manual adjustment)
    .replace(/!\[([^\]]*)\]\(([^)]+)\)/g, '![$1]($2)');
}

/**
 * PULL: Copy READMEs from GitHub repo to site/content/
 */
function pull() {
  console.log('📥 Pulling content from GitHub READMEs...\n');
  
  let synced = 0;
  let skipped = 0;
  let errors = 0;
  
  for (const [githubPath, sitePath] of Object.entries(SYNC_MAP)) {
    const srcFile = path.join(ROOT, githubPath);
    const destFile = path.join(SITE_CONTENT, sitePath);
    
    if (!fs.existsSync(srcFile)) {
      console.log(`  ⚠️  Source not found: ${githubPath}`);
      skipped++;
      continue;
    }
    
    // Read source
    let content = fs.readFileSync(srcFile, 'utf-8');
    
    // Extract title from first heading
    const titleMatch = content.match(/^#\s+(.+)/m);
    const title = titleMatch ? titleMatch[1].replace(/[🟢🔴🔵🟣🤖⚙️🛡️🚀🧪]/g, '').trim() : path.basename(sitePath, '.md');
    
    // Add frontmatter if needed
    content = addFrontmatter(content, title);
    
    // Transform links
    content = transformLinks(content, githubPath);
    
    // Ensure directory exists
    const destDir = path.dirname(destFile);
    fs.mkdirSync(destDir, { recursive: true });
    
    // Write file
    fs.writeFileSync(destFile, content, 'utf-8');
    console.log(`  ✅ ${githubPath} → ${sitePath}`);
    synced++;
  }
  
  console.log(`\n📊 Sync complete: ${synced} synced, ${skipped} skipped, ${errors} errors`);
}

/**
 * STATUS: Show what's different between GitHub and site content
 */
function status() {
  console.log('📊 Sync Status\n');
  
  let inSync = 0;
  let diverged = 0;
  let webOnly = 0;
  let githubOnly = 0;
  
  for (const [githubPath, sitePath] of Object.entries(SYNC_MAP)) {
    const srcFile = path.join(ROOT, githubPath);
    const destFile = path.join(SITE_CONTENT, sitePath);
    
    const srcExists = fs.existsSync(srcFile);
    const destExists = fs.existsSync(destFile);
    
    if (srcExists && destExists) {
      // Compare content (ignoring frontmatter)
      const srcContent = fs.readFileSync(srcFile, 'utf-8').replace(/^---[\s\S]*?---\n/, '');
      const destContent = fs.readFileSync(destFile, 'utf-8').replace(/^---[\s\S]*?---\n/, '');
      
      if (srcContent.trim() === destContent.trim()) {
        console.log(`  ✅ ${githubPath} — in sync`);
        inSync++;
      } else {
        console.log(`  ⚠️  ${githubPath} — DIVERGED`);
        diverged++;
      }
    } else if (!srcExists && destExists) {
      console.log(`  🌐 ${sitePath} — web only (no GitHub source)`);
      webOnly++;
    } else if (srcExists && !destExists) {
      console.log(`  📦 ${githubPath} — GitHub only (not synced)`);
      githubOnly++;
    }
  }
  
  console.log(`\n📊 Summary: ${inSync} synced, ${diverged} diverged, ${webOnly} web-only, ${githubOnly} github-only`);
}

/**
 * BUILD: Pull + VitePress build
 */
function build() {
  console.log('🔨 Building site...\n');
  pull();
  console.log('\n🏗️  Running VitePress build...\n');
  execSync('npx vitepress build content', { cwd: __dirname, stdio: 'inherit' });
  console.log('\n✅ Build complete! Output in docs/');
}

// CLI
const command = process.argv[2];

switch (command) {
  case 'pull':
    pull();
    break;
  case 'status':
    status();
    break;
  case 'build':
    build();
    break;
  default:
    console.log(`
CDPN Sync System
================

Usage: node sync.js <command>

Commands:
  pull     Copy GitHub READMEs → site/content/
  status   Show sync status between GitHub and web
  build    Pull content + VitePress build
  
Examples:
  node sync.js pull      # Sync READMEs to web
  node sync.js status    # Check what's out of sync
  node sync.js build     # Full build for deployment
    `);
}
