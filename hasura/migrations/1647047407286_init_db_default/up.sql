ALTER TABLE electric_power_sale_contract
    ALTER created_at SET DEFAULT Now(),
    ALTER price_common SET DEFAULT 0.0,
    ALTER price_peak SET DEFAULT 0.0,
    ALTER price_flat SET DEFAULT 0.0,
    ALTER price_valley SET DEFAULT 0.0,
    ALTER created_at SET DEFAULT Now(),
    ALTER is_active SET DEFAULT true;