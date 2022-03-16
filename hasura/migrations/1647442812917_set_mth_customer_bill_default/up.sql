ALTER TABLE electric_power_sale_mthcustomerbill
    ALTER  state SET DEFAULT 'draft',
    ALTER created_at SET DEFAULT Now(),
    ALTER updated_at SET DEFAULT Now();
 
ALTER TABLE electric_power_sale_mthdraftcustomerbillline
    ALTER state SET DEFAULT 'draft',
    ALTER created_at SET DEFAULT Now(),
    ALTER updated_at SET DEFAULT Now(),
    ALTER act_common SET DEFAULT 0.0,
    ALTER act_flat SET DEFAULT 0.0,
    ALTER act_valley SET DEFAULT 0.0,
    ALTER act_peak SET DEFAULT 0.0;