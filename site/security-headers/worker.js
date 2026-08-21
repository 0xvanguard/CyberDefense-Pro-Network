/**
 * Cloudflare Worker — Security Headers for CDPN
 * 
 * Adds security headers to all responses from GitHub Pages.
 * 
 * Setup:
 * 1. Create a Cloudflare Worker at dash.cloudflare.com
 * 2. Paste this code
 * 3. Add a Custom Domain or Route to your GitHub Pages domain
 * 
 * Headers added:
 * - Content-Security-Policy (CSP)
 * - X-Frame-Options
 * - X-Content-Type-Options
 * - Referrer-Policy
 * - Permissions-Policy
 * - Cross-Origin-Opener-Policy
 * - Cross-Origin-Resource-Policy
 * - Cross-Origin-Embedder-Policy
 * - Cache-Control (for sensitive pages)
 */

const SECURITY_HEADERS = {
  // Content Security Policy - restricts resource loading
  'Content-Security-Policy': [
    "default-src 'self'",
    "script-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdnjs.cloudflare.com https://www.googletagmanager.com https://www.google-analytics.com",
    "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdnjs.cloudflare.com",
    "font-src 'self' https://fonts.gstatic.com https://cdnjs.cloudflare.com",
    "img-src 'self' data: https: blob:",
    "connect-src 'self' https://api.github.com https://www.google-analytics.com",
    "media-src 'self'",
    "object-src 'none'",
    "frame-src 'none'",
    "frame-ancestors 'none'",
    "form-action 'self'",
    "base-uri 'self'",
    "upgrade-insecure-requests"
  ].join('; '),

  // Prevent clickjacking
  'X-Frame-Options': 'DENY',

  // Prevent MIME type sniffing
  'X-Content-Type-Options': 'nosniff',

  // Control referrer information
  'Referrer-Policy': 'strict-origin-when-cross-origin',

  // Restrict browser features
  'Permissions-Policy': [
    'camera=()',
    'microphone=()',
    'geolocation=()',
    'payment=()',
    'usb=()',
    'magnetometer=()',
    'gyroscope=()',
    'accelerometer=()',
    'ambient-light-sensor=()',
    'autoplay=()',
    'battery=()',
    'display-capture=()',
    'encrypted-media=()',
    'fullscreen=(self)',
    'gamepad=()',
    'midi=()',
    'picture-in-picture=()',
    'speaker=()',
    'sync-xhr=()',
    'web-share=()',
    'xr-spatial-tracking=()'
  ].join(', '),

  // Isolate browsing context
  'Cross-Origin-Opener-Policy': 'same-origin',

  // Prevent cross-origin reads
  'Cross-Origin-Resource-Policy': 'same-origin',

  // Require CORS for cross-origin resources
  'Cross-Origin-Embedder-Policy': 'require-corp',

  // Strict Transport Security (HTTPS only)
  'Strict-Transport-Security': 'max-age=31536000; includeSubDomains; preload',

  // Remove server identification
  'Server': 'Cloudflare',
};

// Headers for admin page (more restrictive)
const ADMIN_HEADERS = {
  'Cache-Control': 'no-store, no-cache, must-revalidate, private',
  'Pragma': 'no-cache',
  'X-Robots-Tag': 'noindex, nofollow, noarchive, nosnippet',
};

// Headers for API responses
const API_HEADERS = {
  'Access-Control-Allow-Origin': 'https://0xvanguard.github.io',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, Authorization',
  'Access-Control-Max-Age': '86400',
};

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;

    // Handle CORS preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, {
        status: 204,
        headers: {
          ...API_HEADERS,
          'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        },
      });
    }

    // Fetch the original response
    const response = await fetch(request);
    
    // Create new response with security headers
    const newResponse = new Response(response.body, response);
    
    // Add security headers
    Object.entries(SECURITY_HEADERS).forEach(([key, value]) => {
      newResponse.headers.set(key, value);
    });

    // Add admin-specific headers
    if (path.includes('admin')) {
      Object.entries(ADMIN_HEADERS).forEach(([key, value]) => {
        newResponse.headers.set(key, value);
      });
    }

    // Add API headers for GitHub API proxy (if used)
    if (path.startsWith('/api/')) {
      Object.entries(API_HEADERS).forEach(([key, value]) => {
        newResponse.headers.set(key, value);
      });
    }

    // Remove potentially dangerous headers
    newResponse.headers.delete('X-Powered-By');
    newResponse.headers.delete('Server');

    return newResponse;
  },
};
