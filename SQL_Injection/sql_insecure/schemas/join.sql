SELECT Users.email, Users.user_name, Auth.password
FROM Users
INNER JOIN Auth ON Users.email = Auth.email;

SELECT Users.email, Users.user_name, Auth.password, Languages.language
FROM Users
INNER JOIN Languages on Users.email = Languages.email
INNER JOIN Auth on Users.email = Auth.email;
