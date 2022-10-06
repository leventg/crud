CREATE TABLE IF NOT EXISTS listings (
	id INTEGER PRIMARY KEY,
   	address text NOT NULL,
	price INTEGER DEFAULT 0,
	table_constraints
)