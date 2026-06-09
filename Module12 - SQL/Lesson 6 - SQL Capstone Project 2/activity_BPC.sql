DROP TABLE IF EXISTS Restaurant;

-- Create Restaurant table
CREATE TABLE IF NOT EXISTS Restaurant (
  name TEXT,
  neighborhood TEXT,
  cuisine TEXT,
  review REAL,
  price TEXT,
  health TEXT
);

-- Insert data
INSERT INTO Restaurant (name, neighborhood, cuisine, review, price, health)
VALUES
  ('Peter', 'Brooklyn', 'Steak', 4.4, '$$$$', 'A'),
  ('Jongro', 'Midtown', 'Korean', 3.5, '$$', 'A'),
  ('Pocha', 'Midtown', 'Pizza', 4.0, '$$$', 'B'),
  ('Lighthouse', 'Queens', 'Chinese', 3.9, '$', 'A'),
  ('Minca', 'Downtown', 'American', 4.6, '$$$', ''),
  ('Marea', 'Chinatown', 'Chinese', 3.0, '$$', ''),
  ('Dirty Candy', 'Uptown', 'Italian', 4.9, '$$$$', 'B'),
  ('Di Fara Pizza', 'Brooklyn', 'Pizza', 3.8, '$$', 'A'),
  ('Golden Unicorn', 'Uptown', 'Italian', 3.8, '$$', 'A');

-- BASED ON THE DATA ABOVE, LET'S ANSWER THE FOLLOWING QUESTIONS

-- 1) What are the distinct (or unique) neighborhoods?

-- 2) What are the distinct cuisine types?

-- 3) What are the options for Chinese takeout?

-- 4) Which restaurants have reviews 4 and above?

-- 5) Which Italian restaurants have a price category $$ or $$$

-- 6) Which restaurants with exactly $$$ price category?

-- 7) Which restaurants contain "Candy" in their names?

-- 8) Which restaurants in Midtown, Downtown, or Chinatown?

-- 9) Which restaurants have Health grade pending (empty value)?

-- 10) Find the top 4 restaurants based on reviews