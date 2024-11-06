USE mysql;
USE ETextBook;

-- Create the stored procedure to insert a new user
DELIMITER $$

CREATE PROCEDURE AddUser(
    IN p_userID VARCHAR(20),
    IN p_firstName VARCHAR(20),
    IN p_lastName VARCHAR(20),
    IN p_email VARCHAR(50),
    IN p_password VARCHAR(20),
    IN p_role TEXT
)
BEGIN
    -- Insert into User table
    INSERT INTO ETextBook.User (userID, firstName, lastName, email, password, role)
    VALUES (p_userID, p_firstName, p_lastName, p_email, p_password, p_role);
END$$

DELIMITER ;
