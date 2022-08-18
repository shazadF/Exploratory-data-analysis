SELECT platform_country_code, SUM(booking_rev_EURcent) as total_rev FROM `Trivago` GROUP BY platform_country_code order BY total_rev DESC LIMIT 3

task 2a - SELECT adv_id, SUM(booking_rev_EURcent) - (SUM(booking_rev_EURcent)*0.15) as total_rev FROM `Trivago` GROUP BY adv_id order BY total_rev DESC