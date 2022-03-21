ALTER TABLE electric_power_sale_mthagentbill
    ALTER  state SET DEFAULT 'draft',
    ALTER created_at SET DEFAULT Now(),
    ALTER updated_at SET DEFAULT Now();
 
ALTER TABLE electric_power_sale_mthagentbillline
    ALTER state SET DEFAULT 'draft',
    ALTER created_at SET DEFAULT Now(),
    ALTER updated_at SET DEFAULT Now(),
    ALTER act_common SET DEFAULT 0.0,
    ALTER act_flat SET DEFAULT 0.0,
    ALTER act_valley SET DEFAULT 0.0,
    ALTER act_peak SET DEFAULT 0.0,
    ALTER price_common SET DEFAULT 0.0,
    ALTER price_peak SET DEFAULT 0.0,
    ALTER price_flat SET DEFAULT 0.0,
    ALTER price_valley SET DEFAULT 0.0,
    ALTER service_rate SET DEFAULT 0.0,
    ALTER service_fee SET DEFAULT 0.0,
    ALTER agent_rate SET DEFAULT 0.0,
    ALTER agent_fee SET DEFAULT 0.0,
    ALTER tax_diff SET DEFAULT 0.0,
    ALTER act_agent_fee SET DEFAULT 0.0;