-- Create a function named SafeDiv that takes two integers as input and returns the result of the division of the first number by the second number. If the second number is 0, the function should return 0.
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END$$
DELIMITER ;
