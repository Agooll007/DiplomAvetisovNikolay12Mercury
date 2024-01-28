# Задание 1
SELECT c.login, count(o.id)
FROM "Couriers" c JOIN "Orders" o on (o."courierId" = c.id) AND o."inDelivery" = true;

# Задание 2
SELECT track,
  CASE
    WHEN finished = true THEN 2
    WHEN cancelled = true THEN -1
    WHEN "inDelivery" = true THEN 1
    ELSE 0
  END AS status
FROM "Orders";