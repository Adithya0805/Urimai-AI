-- Migration 005: Add agriculture fields to persons table
-- Additive extension: land_holding_acres and crop_type

ALTER TABLE persons ADD COLUMN IF NOT EXISTS land_holding_acres NUMERIC(6, 2) DEFAULT 0.0;
ALTER TABLE persons ADD COLUMN IF NOT EXISTS crop_type VARCHAR(100) DEFAULT NULL;
