-- Create an index on the name column of the names table and on first character 
DROP INDEX idx_name_first ON names;
CREATE INDEX idx_name_first ON  names(name(1));
