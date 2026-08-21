#!/usr/bin/env node
/**
 * Post-build script: converts flat .html files to directory-style
 * for GitHub Pages clean URL support.
 * 
 * recon-01.html → recon-01/index.html
 * This allows URLs like /campus/labs/intermedio/recon-01/ to work.
 * 
 * Also fixes sidebar links that VitePress renders with .html extensions
 * but that break after the file conversion (since files are now at
 * file/index.html instead of file.html).
 */

const fs = require('fs');
const path = require('path');

const CAMPUS_DIR = path.resolve(__dirname, '../docs/campus');

function convertToCleanUrls(dir) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  let converted = 0;

  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);

    if (entry.isDirectory()) {
      // Always recurse into directories to convert nested .html files
      converted += convertToCleanUrls(fullPath);
    } else if (entry.name.endsWith('.html') && entry.name !== 'index.html' && entry.name !== 'admin.html') {
      // Convert file.html → file/index.html
      const dirName = entry.name.replace('.html', '');
      const targetDir = path.join(dir, dirName);
      const targetFile = path.join(targetDir, 'index.html');

      if (!fs.existsSync(targetDir)) {
        fs.mkdirSync(targetDir, { recursive: true });
      }

      // Move the file
      fs.renameSync(fullPath, targetFile);
      converted++;
      console.log(`  📁 ${path.relative(CAMPUS_DIR, fullPath)} → ${path.relative(CAMPUS_DIR, targetFile)}`);
    }
  }

  return converted;
}

/**
 * Fix sidebar links: VitePress renders links with .html extensions,
 * but after convertToCleanUrls those files are now at file/index.html.
 * We need to strip .html from href attributes in sidebar/nav links.
 */
function fixSidebarLinks(dir) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  let fixed = 0;

  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);

    if (entry.isDirectory()) {
      fixed += fixSidebarLinks(fullPath);
    } else if (entry.name.endsWith('.html')) {
      let content = fs.readFileSync(fullPath, 'utf-8');
      let modified = false;

      // Fix sidebar/nav links: href="/CyberDefense-Pro-Network/campus/...foo.html"
      // → href="/CyberDefense-Pro-Network/campus/...foo/"
      // But only for links that point to files we converted (not external links)
      const base = '/CyberDefense-Pro-Network/campus/';
      const newContent = content.replace(
        new RegExp(`href="(${escapeRegex(base)}[^"]+?)\.html"`, 'g'),
        (match, urlPath) => {
          // Check if the target file was converted to a directory
          const localPath = path.join(CAMPUS_DIR, urlPath + '.html');
          const targetDir = path.join(CAMPUS_DIR, urlPath);
          // Convert: the .html file is now at urlPath/index.html
          // So strip .html and add /
          return `href="${urlPath}/"`;
        }
      );

      if (newContent !== content) {
        fs.writeFileSync(fullPath, newContent, 'utf-8');
        modified = true;
        fixed++;
      }
    }
  }

  return fixed;
}

function escapeRegex(str) {
  return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

console.log('🔄 Converting to clean URLs for GitHub Pages...\n');
const count = convertToCleanUrls(CAMPUS_DIR);
console.log(`\n✅ Converted ${count} files to directory-style URLs`);

console.log('\n🔧 Fixing sidebar links (.html → clean URLs)...\n');
const fixed = fixSidebarLinks(CAMPUS_DIR);
console.log(`\n✅ Fixed ${fixed} files with .html sidebar links`);
