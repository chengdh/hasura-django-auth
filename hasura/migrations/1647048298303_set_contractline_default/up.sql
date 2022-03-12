ALTER TABLE electric_power_sale_contractline
    ALTER  plan_common SET DEFAULT 0.0,
    ALTER  plan_flat SET DEFAULT 0.0,
    ALTER  plan_valley SET DEFAULT 0.0,
    ALTER  plan_peak SET DEFAULT 0.0,
    ALTER  adjust_plan_common SET DEFAULT 0.0,
    ALTER  adjust_plan_flat SET DEFAULT 0.0,
    ALTER  adjust_plan_valley SET DEFAULT 0.0,
    ALTER  adjust_plan_peak SET DEFAULT 0.0,
    ALTER  act_common SET DEFAULT 0.0,
    ALTER  act_flat SET DEFAULT 0.0,
    ALTER  act_valley SET DEFAULT 0.0,
    ALTER  act_peak SET DEFAULT 0.0,
    ALTER  price_common SET DEFAULT 0.0,
    ALTER  price_peak SET DEFAULT 0.0,
    ALTER  price_flat SET DEFAULT 0.0,
    ALTER  price_valley SET DEFAULT 0.0;
    ALTER  'state' SET DEFAULT "confirmed";


ALTER TABLE electric_power_sale_contract
    ALTER  'state' SET DEFAULT "confirmed";