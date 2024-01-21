-- creates a trigger
DELIMITER $$
CREATE TRIGGER reset
BEFORE UPDATE
ON users
FOR EACH ROW
IF OLD.email != NEW.email THEN
SET NEW.valid_email = 0;
END IF;
$$
DELIMITER ;
