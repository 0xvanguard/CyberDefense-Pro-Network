# ================================================
# Dockerfile para Lab de Escalada de Privilegios Windows
# NOTA: Este es un ejemplo simplificado.
# En producción, usar imágenes oficiales de Microsoft.
# ================================================

FROM mcr.microsoft.com/windows/servercore:ltsc2019

# Instalar herramientas básicas
RUN powershell -Command \
    Set-ExecutionPolicy Bypass -Scope Process -Force; \
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; \
    Invoke-WebRequest -Uri "https://github.com/PowerShell/PowerShell/releases/download/v7.3.0/PowerShell-7.3.0-win-x64.msi" -OutFile "$env:TEMP\pwsh.msi"; \
    Start-Process msiexec.exe -Wait -ArgumentList "$env:TEMP\pwsh.msi /quiet"; \
    Remove-Item "$env:TEMP\pwsh.msi"

# Crear usuario de bajo nivel
RUN net user lowuser Password123 /add && \
    net localgroup Administrators lowuser /delete

# ============================================
# VULNERABILIDAD 1: Unquoted Service Path
# ============================================
RUN mkdir "C:\Program Files\Vuln Service" && \
    echo @echo off > "C:\Program Files\Vuln Service\service.exe" && \
    echo echo Vulnerable Service Running >> "C:\Program Files\Vuln Service\service.exe" && \
    sc create VulnService binPath= "C:\Program Files\Vuln Service\service.exe" start= auto

# ============================================
# VULNERABILIDAD 2: Modificable Service Binary
# ============================================
RUN mkdir "C:\VulnService" && \
    echo @echo off > "C:\VulnService\service.exe" && \
    echo echo Modifiable Service >> "C:\VulnService\service.exe" && \
    sc create ModifiableService binPath= "C:\VulnService\service.exe" start= auto

# Dar permisos de escritura a usuarios estándar
RUN icacls "C:\VulnService" /grant "Everyone:(OI)(CI)F" /T

# ============================================
# VULNERABILIDAD 3: AlwaysInstallElevated
# ============================================
RUN reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer" /v AlwaysInstallElevated /t REG_DWORD /d 1 /f && \
    reg add "HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer" /v AlwaysInstallElevated /t REG_DWORD /d 1 /f

# ============================================
# VULNERABILIDAD 4: Autorun Program
# ============================================
RUN reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v VulnAutostart /t REG_SZ /d "C:\VulnService\service.exe" /f

# ============================================
# VULNERABILIDAD 5: Stored Credentials
# ============================================
RUN cmdkey /generic:TERMSRV/localhost /user:admin /pass:SuperSecret123

# Flag para el lab
RUN echo FLAG{pr1v3sc_w1nd0ws_l4b_c0mpl3t3d} > C:\Users\Administrator\Desktop\flag.txt

# Configurar WinRM
RUN powershell -Command \
    Enable-PSRemoting -Force; \
    Set-Item WSMan:\localhost\Service\Auth\Basic -Value $true; \
    Set-Item WSMan:\localhost\Service\AllowUnencrypted -Value $true

EXPOSE 3389 5985

CMD ["powershell", "-Command", "while($true){Start-Sleep -Seconds 3600}"]
