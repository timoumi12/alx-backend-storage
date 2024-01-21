-- creates a stored procedure AddBonus
DELIMITER $$
CREATE PROCEDURE AddBonus(user_id INT, project_name varchar(255), score INT)
BEGIN
    -- if no projects.name found in the table, create it
    INSERT INTO projects(name)
    SELECT project_name FROM DUAL
    WHERE NOT EXISTS(
        SELECT * FROM projects WHERE name = project_name LIMIT 1
    );
    -- adds a new correction for a student
    INSERT INTO corrections(user_id, project_id, score)
    VALUES(
        user_id,
        SELECT id FROM projects WHERE name = project_name),
        score
    );
END $$
DELIMITER ;

