#!/usr/bin/env python3
"""
🔒 Docker Security Migration Script
CyberDefense Pro Network

Este script actualiza automáticamente todos los docker-compose.yml
con las mejores prácticas de seguridad.

Uso:
    python3 migrate-docker-security.py
"""

import os
import re
import yaml
import sys
from pathlib import Path
from typing import Dict, Any, Optional

# ============================================
# Security Configuration
# ============================================

DEFAULT_SECURITY_CONFIG = {
    'deploy': {
        'resources': {
            'limits': {
                'cpus': '1.0',
                'memory': '512M'
            },
            'reservations': {
                'cpus': '0.25',
                'memory': '128M'
            }
        }
    },
    'cap_drop': ['ALL'],
    'security_opt': ['no-new-privileges:true'],
    'healthcheck': {
        'test': ['CMD', 'curl', '-f', 'http://localhost/'],
        'interval': '30s',
        'timeout': '10s',
        'retries': 3,
        'start_period': '40s'
    },
    'logging': {
        'driver': 'json-file',
        'options': {
            'max-size': '10m',
            'max-file': '3'
        }
    },
    'restart': 'unless-stopped'
}

# Service-specific configurations
SERVICE_CONFIGS = {
    'kali': {
        'deploy': {
            'resources': {
                'limits': {'cpus': '2.0', 'memory': '1G'},
                'reservations': {'cpus': '0.5', 'memory': '256M'}
            }
        },
        'cap_add': ['NET_RAW', 'NET_ADMIN'],
        'healthcheck': {
            'test': ['CMD', 'pgrep', 'bash'],
            'interval': '30s',
            'timeout': '5s',
            'retries': 3
        }
    },
    'mysql': {
        'deploy': {
            'resources': {
                'limits': {'cpus': '0.5', 'memory': '256M'},
                'reservations': {'cpus': '0.1', 'memory': '64M'}
            }
        },
        'cap_add': ['NET_BIND_SERVICE', 'SYS_NICE'],
        'healthcheck': {
            'test': ['CMD', 'mysqladmin', 'ping', '-h', 'localhost'],
            'interval': '30s',
            'timeout': '10s',
            'retries': 3,
            'start_period': '30s'
        }
    },
    'nginx': {
        'cap_add': ['NET_BIND_SERVICE'],
        'healthcheck': {
            'test': ['CMD', 'curl', '-f', 'http://localhost/'],
            'interval': '30s',
            'timeout': '10s',
            'retries': 3,
            'start_period': '30s'
        }
    },
    'apache': {
        'cap_add': ['NET_BIND_SERVICE'],
        'healthcheck': {
            'test': ['CMD', 'curl', '-f', 'http://localhost/'],
            'interval': '30s',
            'timeout': '10s',
            'retries': 3,
            'start_period': '30s'
        }
    },
    'wazuh': {
        'deploy': {
            'resources': {
                'limits': {'cpus': '1.0', 'memory': '1G'},
                'reservations': {'cpus': '0.25', 'memory': '256M'}
            }
        },
        'healthcheck': {
            'test': ['CMD', 'curl', '-f', 'http://localhost:55000'],
            'interval': '30s',
            'timeout': '10s',
            'retries': 3,
            'start_period': '60s'
        }
    },
    'postgres': {
        'deploy': {
            'resources': {
                'limits': {'cpus': '0.5', 'memory': '256M'},
                'reservations': {'cpus': '0.1', 'memory': '64M'}
            }
        },
        'cap_add': ['NET_BIND_SERVICE', 'SYS_NICE'],
        'healthcheck': {
            'test': ['CMD-SHELL', 'pg_isready -U postgres'],
            'interval': '30s',
            'timeout': '10s',
            'retries': 3,
            'start_period': '30s'
        }
    },
    'redis': {
        'deploy': {
            'resources': {
                'limits': {'cpus': '0.25', 'memory': '128M'},
                'reservations': {'cpus': '0.05', 'memory': '32M'}
            }
        },
        'healthcheck': {
            'test': ['CMD', 'redis-cli', 'ping'],
            'interval': '30s',
            'timeout': '5s',
            'retries': 3
        }
    },
    'mongodb': {
        'deploy': {
            'resources': {
                'limits': {'cpus': '0.5', 'memory': '512M'},
                'reservations': {'cpus': '0.1', 'memory': '128M'}
            }
        },
        'healthcheck': {
            'test': ['CMD', 'mongo', '--eval', 'db.adminCommand("ping")'],
            'interval': '30s',
            'timeout': '10s',
            'retries': 3,
            'start_period': '30s'
        }
    }
}

# ============================================
# Helper Functions
# ============================================

def load_docker_compose(file_path: str) -> Optional[Dict[str, Any]]:
    """Load a docker-compose.yml file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # Fix common YAML issues
            content = f.read()
            # Remove invalid characters
            content = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', content)
            return yaml.safe_load(content)
    except Exception as e:
        print(f"  ⚠️  Error loading {file_path}: {e}")
        return None

def save_docker_compose(file_path: str, data: Dict[str, Any]) -> bool:
    """Save a docker-compose.yml file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        return True
    except Exception as e:
        print(f"  ⚠️  Error saving {file_path}: {e}")
        return False

def get_service_type(service_name: str, service_config: Dict[str, Any]) -> str:
    """Determine the type of service based on name and image."""
    name_lower = service_name.lower()
    image = service_config.get('image', '').lower()
    
    # Check by name
    for service_type in SERVICE_CONFIGS:
        if service_type in name_lower:
            return service_type
    
    # Check by image
    if 'mysql' in image or 'mariadb' in image:
        return 'mysql'
    elif 'postgres' in image:
        return 'postgres'
    elif 'redis' in image:
        return 'redis'
    elif 'mongo' in image:
        return 'mongodb'
    elif 'nginx' in image:
        return 'nginx'
    elif 'apache' in image or 'httpd' in image:
        return 'apache'
    elif 'wazuh' in image:
        return 'wazuh'
    elif 'kali' in image:
        return 'kali'
    
    return 'default'

def apply_security_config(service_name: str, service_config: Dict[str, Any]) -> Dict[str, Any]:
    """Apply security configuration to a service."""
    # Get service type
    service_type = get_service_type(service_name, service_config)
    config = SERVICE_CONFIGS.get(service_type, {})
    
    # Merge configurations (service-specific overrides defaults)
    for key, value in DEFAULT_SECURITY_CONFIG.items():
        if key not in service_config:
            service_config[key] = value
        elif isinstance(value, dict) and isinstance(service_config[key], dict):
            # Merge dictionaries
            for k, v in value.items():
                if k not in service_config[key]:
                    service_config[key][k] = v
    
    # Apply service-specific config
    for key, value in config.items():
        if key == 'deploy':
            # Merge deploy resources
            if 'deploy' not in service_config:
                service_config['deploy'] = value
            elif 'resources' not in service_config['deploy']:
                service_config['deploy']['resources'] = value.get('resources', {})
        elif key == 'cap_add':
            # Add capabilities without removing existing ones
            existing = service_config.get('cap_add', [])
            service_config['cap_add'] = list(set(existing + value))
        elif key == 'healthcheck':
            if 'healthcheck' not in service_config:
                service_config['healthcheck'] = value
        else:
            if key not in service_config:
                service_config[key] = value
    
    # Ensure cap_drop includes ALL
    if 'cap_drop' not in service_config:
        service_config['cap_drop'] = ['ALL']
    elif 'ALL' not in service_config['cap_drop']:
        service_config['cap_drop'].insert(0, 'ALL')
    
    return service_config

def create_env_file(file_path: str, services: Dict[str, Any]) -> bool:
    """Create a .env.example file for the lab."""
    env_path = os.path.join(os.path.dirname(file_path), '.env.example')
    
    if os.path.exists(env_path):
        return True  # Already exists
    
    env_content = """# 🔒 Environment Variables
# CyberDefense Pro Network - Docker Labs
#
# Instrucciones:
#   1. Copiar este archivo como .env
#   2. Modificar los valores
#   3. NUNCA subir .env a git

# Lab Configuration
LAB_NAME=lab

# Database Credentials
MYSQL_ROOT_PASSWORD=CHANGE_ME_$(openssl rand -base64 32)
MYSQL_DATABASE=lab
MYSQL_USER=labuser
MYSQL_PASSWORD=CHANGE_ME_$(openssl rand -base64 32)

# Application Credentials
ADMIN_PASSWORD=CHANGE_ME_$(openssl rand -base64 32)

# Ports (to avoid conflicts)
WEB_PORT=8080
DB_PORT=3306
SSH_PORT=2222
"""
    
    try:
        with open(env_path, 'w', encoding='utf-8') as f:
            f.write(env_content)
        return True
    except Exception as e:
        print(f"  ⚠️  Error creating .env.example: {e}")
        return False

# ============================================
# Main Migration Function
# ============================================

def migrate_docker_compose(file_path: str) -> bool:
    """Migrate a single docker-compose.yml file."""
    print(f"\n📝 Processing: {file_path}")
    
    # Load the file
    data = load_docker_compose(file_path)
    if not data:
        return False
    
    # Check if it has services
    if 'services' not in data:
        print(f"  ⚠️  No services found, skipping")
        return False
    
    # Track changes
    changes = []
    
    # Process each service
    for service_name, service_config in data['services'].items():
        original = str(service_config)
        
        # Apply security config
        data['services'][service_name] = apply_security_config(service_name, service_config)
        
        # Check if anything changed
        if str(data['services'][service_name]) != original:
            changes.append(service_name)
    
    # Add version if missing
    if 'version' not in data:
        data['version'] = '3.8'
        changes.append('version')
    
    # Add networks if missing
    if 'networks' not in data:
        data['networks'] = {
            'lab-net': {
                'driver': 'bridge',
                'ipam': {
                    'config': [
                        {'subnet': '10.0.1.0/24'}
                    ]
                }
            }
        }
        changes.append('networks')
    
    # Save the file
    if changes:
        if save_docker_compose(file_path, data):
            print(f"  ✅ Updated {len(changes)} services: {', '.join(changes)}")
            
            # Create .env.example
            create_env_file(file_path, data['services'])
            
            return True
        else:
            return False
    else:
        print(f"  ℹ️  No changes needed")
        return True

def main():
    """Main function."""
    print("🔒 Docker Security Migration Script")
    print("====================================")
    
    # Find all docker-compose files
    labs_dir = Path('site/content/labs')
    docker_files = list(labs_dir.rglob('docker-compose.yml'))
    
    print(f"\n📊 Found {len(docker_files)} docker-compose files")
    
    # Process each file
    success = 0
    failed = 0
    skipped = 0
    
    for docker_file in docker_files:
        # Skip template
        if 'TEMPLATE-SECURE' in str(docker_file):
            print(f"\n⏭️  Skipping template: {docker_file}")
            skipped += 1
            continue
        
        # Skip already processed files (check for security config)
        try:
            with open(docker_file, 'r') as f:
                content = f.read()
                if 'cap_drop:' in content and 'healthcheck:' in content:
                    print(f"\n⏭️  Already secured: {docker_file}")
                    skipped += 1
                    continue
        except:
            pass
        
        # Migrate the file
        if migrate_docker_compose(str(docker_file)):
            success += 1
        else:
            failed += 1
    
    # Print summary
    print("\n" + "="*40)
    print("📊 Migration Summary")
    print("="*40)
    print(f"✅ Success: {success}")
    print(f"⚠️  Skipped: {skipped}")
    print(f"❌ Failed: {failed}")
    print(f"📁 Total: {len(docker_files)}")
    print("\n🔒 Security improvements applied:")
    print("  - Resource limits (CPU/Memory)")
    print("  - Capability drops (cap_drop: ALL)")
    print("  - Security options (no-new-privileges)")
    print("  - Healthchecks")
    print("  - Logging configuration")
    print("  - Restart policies")
    print("  - .env.example files")
    print("\n📋 Next steps:")
    print("  1. Review each migrated file")
    print("  2. Test with: docker compose up -d")
    print("  3. Verify healthchecks: docker compose ps")

if __name__ == '__main__':
    main()
