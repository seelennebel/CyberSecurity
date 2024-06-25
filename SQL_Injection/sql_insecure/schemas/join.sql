SELECT Users.email, Users.user_name, Auth.password
FROM Users
INNER JOIN Auth ON Users.email = Auth.email;