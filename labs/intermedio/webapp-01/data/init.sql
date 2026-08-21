-- Database schema for VulnShop
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100),
    role ENUM('admin', 'user', 'guest') DEFAULT 'user',
    bio TEXT
);

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2),
    description TEXT
);

CREATE TABLE IF NOT EXISTS comments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS invoices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    amount DECIMAL(10,2),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert test data
INSERT INTO users (username, password, email, role, bio) VALUES
('admin', '5f4dcc3b5aa765d61d8327deb882cf99', 'admin@vulnshop.local', 'admin', 'Administrator of VulnShop'),
('user1', 'e10adc3949ba59abbe56e057f20f883e', 'user1@vulnshop.local', 'user', 'Regular customer'),
('user2', 'd8578edf8458ce06fbc5bb76a58c5ca4', 'user2@vulnshop.local', 'user', 'Premium customer'),
('guest', 'guest123', 'guest@vulnshop.local', 'guest', 'Guest account');

INSERT INTO products (name, price, description) VALUES
('Laptop Pro', 1299.99, 'High-performance laptop'),
('Wireless Mouse', 29.99, 'Ergonomic wireless mouse'),
('USB-C Hub', 49.99, '7-in-1 USB-C hub'),
('Security Camera', 199.99, 'HD security camera'),
('Encryption Key', 9.99, 'Hardware encryption key');

INSERT INTO invoices (user_id, amount, description) VALUES
(1, 1349.98, 'Laptop Pro + USB-C Hub'),
(2, 229.98, 'Security Camera + Mouse'),
(3, 1299.99, 'Laptop Pro');

INSERT INTO comments (message) VALUES
('Welcome to VulnShop forum!'),
('Great products here.'),
('Has anyone tried the encryption key?');
