FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Instalar Apache, PHP y herramientas
RUN apt-get update && apt-get install -y \
    apache2 \
    php \
    libapache2-mod-php \
    php-mysql \
    php-curl \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Crear aplicación vulnerable
RUN mkdir -p /var/www/html/vulnerable

# Login vulnerable (SQL Injection)
RUN cat > /var/www/html/vulnerable/login.php << 'PHP'
<?php
$conn = new mysqli("database", "webapp", "webapp123", "vulnerable_db");

if(isset($_POST['username']) && isset($_POST['password'])) {
    $user = $_POST['username'];
    $pass = $_POST['password'];
    
    // SQL INJECTION VULNERABILITY
    $sql = "SELECT * FROM users WHERE username='$user' AND password='$pass'";
    $result = $conn->query($sql);
    
    if($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        if($row['role'] == 'admin') {
            header("Location: admin/dashboard.php");
        } else {
            header("Location: user/dashboard.php");
        }
    } else {
        $error = "Invalid credentials";
    }
}
?>
<!DOCTYPE html>
<html>
<head><title>Login</title></head>
<body>
    <h1>Login</h1>
    <?php if(isset($error)) echo "<p style='color:red'>$error</p>"; ?>
    <form method="POST">
        <input type="text" name="username" placeholder="Username"><br>
        <input type="password" name="password" placeholder="Password"><br>
        <button type="submit">Login</button>
    </form>
    <p>Hint: Try SQL injection!</p>
</body>
</html>
PHP

# Search vulnerable (XSS + SQL Injection)
RUN cat > /var/www/html/vulnerable/search.php << 'PHP'
<?php
$conn = new mysqli("database", "webapp", "webapp123", "vulnerable_db");

if(isset($_GET['q'])) {
    $query = $_GET['q'];
    // SQL INJECTION
    $sql = "SELECT * FROM products WHERE name LIKE '%$query%'";
    $result = $conn->query($sql);
}
?>
<!DOCTYPE html>
<html>
<head><title>Search</title></head>
<body>
    <h1>Product Search</h1>
    <form method="GET">
        <input type="text" name="q" placeholder="Search products">
        <button type="submit">Search</button>
    </form>
    <?php if(isset($result)): ?>
        <h2>Results:</h2>
        <ul>
        <?php while($row = $result->fetch_assoc()): ?>
            <!-- XSS VULNERABILITY -->
            <li><?= $row['name'] ?> - $<?= $row['price'] ?></li>
        <?php endwhile; ?>
        </ul>
    <?php endif; ?>
    
    <!-- XSS in search term display -->
    <p>You searched for: <?= isset($query) ? $query : '' ?></p>
</body>
</html>
PHP

# Admin panel (Broken Access Control)
RUN mkdir -p /var/www/html/vulnerable/admin
RUN cat > /var/www/html/vulnerable/admin/dashboard.php << 'PHP'
<!DOCTYPE html>
<html>
<head><title>Admin Dashboard</title></head>
<body>
    <h1>Admin Dashboard</h1>
    <p>WARNING: This should be protected!</p>
    <ul>
        <li><a href="users.php">Manage Users</a></li>
        <li><a href="config.php">Configuration</a></li>
    </ul>
</body>
</html>
PHP

# Exposed config file
RUN cat > /var/www/html/vulnerable/config.php << 'PHP'
<?php
// SECURITY MISCONFIGURATION - Exposed credentials
$config = [
    'db_host' => 'database',
    'db_user' => 'webapp',
    'db_pass' => 'webapp123',
    'db_name' => 'vulnerable_db',
    'aws_key' => 'AKIAIOSFODNN7EXAMPLE',
    'aws_secret' => 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
];
?>
PHP

# File upload vulnerable
RUN mkdir -p /var/www/html/vulnerable/upload
RUN cat > /var/www/html/vulnerable/upload.php << 'PHP'
<?php
if(isset($_FILES['file'])) {
    $target = "uploads/" . basename($_FILES["file"]["name"]);
    // NO FILE TYPE VALIDATION
    if(move_uploaded_file($_FILES["file"]["tmp_name"], $target)) {
        echo "File uploaded: <a href='$target'>$target</a>";
    }
}
?>
<!DOCTYPE html>
<html>
<head><title>File Upload</title></head>
<body>
    <h1>Upload File</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <button type="submit">Upload</button>
    </form>
</body>
</html>
PHP

# SSRF vulnerable endpoint
RUN cat > /var/www/html/vulnerable/fetch.php << 'PHP'
<?php
if(isset($_GET['url'])) {
    $url = $_GET['url'];
    // SSRF VULNERABILITY
    $content = file_get_contents($url);
    echo "<pre>$content</pre>";
}
?>
<!DOCTYPE html>
<html>
<head><title>URL Fetcher</title></head>
<body>
    <h1>Fetch URL</h1>
    <form method="GET">
        <input type="text" name="url" placeholder="http://example.com" size="50">
        <button type="submit">Fetch</button>
    </form>
</body>
</html>
PHP

RUN mkdir -p /var/www/html/vulnerable/uploads
RUN chown -R www-data:www-data /var/www/html/vulnerable/uploads

EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND"]
