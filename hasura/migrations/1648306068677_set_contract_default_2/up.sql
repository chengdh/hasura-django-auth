 ALTER TABLE electric_power_sale_contract
    ALTER created_at SET DEFAULT Now(),
    ALTER updated_at SET DEFAULT Now();