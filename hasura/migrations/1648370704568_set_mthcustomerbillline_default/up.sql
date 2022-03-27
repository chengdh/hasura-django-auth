ALTER TABLE electric_power_sale_mthcustomerbillline
    ALTER  state SET DEFAULT 'draft',
    ALTER created_at SET DEFAULT Now(),
    ALTER updated_at SET DEFAULT Now(),
    ALTER price_common SET DEFAULT 0.0, 
    ALTER price_flat SET DEFAULT 0.0, 
    ALTER price_valley SET DEFAULT 0.0, 
    ALTER price_peak SET DEFAULT 0.0, 
    ALTER act_common SET DEFAULT 0.0, 
    ALTER act_flat SET DEFAULT 0.0, 
    ALTER act_valley SET DEFAULT 0.0, 
    ALTER act_peak SET DEFAULT 0.0, 
    ALTER service_rate SET DEFAULT 0.0, 
    ALTER service_fee SET DEFAULT 0.0;