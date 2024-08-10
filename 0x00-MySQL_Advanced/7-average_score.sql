-- Write Write a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
-- Requirements:
-- Your script must create a stored procedure ComputeAverageScoreForUser
-- This stored procedure must take 1 parameter: the user_id
-- The average score must be stored in the average_score column of the users table
-- The average score must be rounded to 2 decimal places
-- The average score must be computed as the average of all the scores of the corrections of the user

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    UPDATE users
    SET average_score = ROUND((SELECT AVG(score) FROM corrections WHERE user_id = user_id), 2)
    WHERE id = user_id;
END$$
DELIMITER ;
