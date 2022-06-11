ALTER TABLE electric_power_sale_contract
    ALTER  state SET DEFAULT 'draft';

ALTER TABLE electric_power_sale_contractline
    ALTER  state SET DEFAULT 'draft';