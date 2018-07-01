BEGIN;
-- protect against concurrent inserts while you update the counter
LOCK TABLE realty_company IN EXCLUSIVE MODE;
-- Update the sequence
SELECT setval('realty_company_id_seq', COALESCE((SELECT MAX(id)+1 FROM realty_company), 1), false);
COMMIT;