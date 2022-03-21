ALTER TABLE electric_power_sale_customer 
    ALTER  rate SET DEFAULT 0.0,
    ALTER  fix_fee SET DEFAULT 0.0,
    ALTER  divide_rate SET DEFAULT 0.0,
    ALTER  agent_rate SET DEFAULT 0.0,
    ALTER  tax_diff SET DEFAULT 0.0,
    ALTER  is_active SET DEFAULT true;

 ALTER TABLE electric_power_sale_agent
    ALTER  default_agent_rate SET DEFAULT 0.0,
    ALTER  is_active SET DEFAULT true;