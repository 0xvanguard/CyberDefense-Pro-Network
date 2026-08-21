#!/usr/bin/env node
/**
 * Post-build script: converts flat .html files to directory-style
 * for GitHub Pages clean URL support.
 * 
 * recon-01.html → recon-01/index.html
 * This allows URLs like /campus/labs/intermedio/recon-01/ to work.
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

console.log('🔄 Converting to clean URLs for GitHub Pages...\n');
const count = convertToCleanUrls(CAMPUS_DIR);
console.log(`\n✅ Converted ${count} files to directory-style URLs`);
