ALTER TABLE electric_power_sale_contractline
    ALTER created_at SET DEFAULT Now(),
    ALTER updated_at SET DEFAULT Now();