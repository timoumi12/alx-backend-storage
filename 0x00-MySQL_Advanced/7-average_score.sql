-- creates a stored procedure AddBonus
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
    -- computes and store the average score for a student
    UPDATE users
	SET
	average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id)
	WHERE id = user_id;
END $$
DELIMITER ;

