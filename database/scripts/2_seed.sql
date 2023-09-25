COPY public.asset_absence_codes(asset_absence_code,asset_absence_code_abbreviation)
FROM '/docker-entrypoint-initdb.d/asset_absence_codes.csv'
DELIMITER ','
CSV HEADER;

COPY public.asset_types(asset_type)
FROM '/docker-entrypoint-initdb.d/asset_types.csv'
DELIMITER ','
CSV HEADER;

COPY public.auth_user
FROM '/docker-entrypoint-initdb.d/auth_user.csv'
DELIMITER ','
CSV HEADER;

COPY public.countries(country,country_code)
FROM '/docker-entrypoint-initdb.d/countries.csv'
DELIMITER ','
CSV HEADER;


COPY public.currencies(currency,currency_abbreviation,currency_account_nr)
FROM '/docker-entrypoint-initdb.d/currencies.csv'
DELIMITER ','
CSV HEADER;

COPY public.django_content_type
FROM '/docker-entrypoint-initdb.d/django_content_type.csv'
DELIMITER ','
CSV HEADER;

COPY public.employee_absence_codes(employee_absence_code,employee_absence_code_abbreviation)
FROM '/docker-entrypoint-initdb.d/employee_absence_codes.csv'
DELIMITER ','
CSV HEADER;

COPY public.employee_types(employee_type_description)
FROM '/docker-entrypoint-initdb.d/employee_types.csv'
DELIMITER ','
CSV HEADER;

COPY public.invoice_states(invoice_state)
FROM '/docker-entrypoint-initdb.d/invoice_states.csv'
DELIMITER ','
CSV HEADER;

COPY public.invoice_terms(due_days,term_title)
FROM '/docker-entrypoint-initdb.d/invoice_terms.csv'
DELIMITER ','
CSV HEADER;

COPY public.sales_state(sales_state)
FROM '/docker-entrypoint-initdb.d/sales_state.csv'
DELIMITER ','
CSV HEADER;

COPY public.sys_rec_states(sys_rec_status,entity)
FROM '/docker-entrypoint-initdb.d/sys_rec_states.csv'
DELIMITER ','
CSV HEADER;

COPY public.task_states(task_state)
FROM '/docker-entrypoint-initdb.d/task_states.csv'
DELIMITER ','
CSV HEADER;

COPY public.units(unit,unit_abbreviation)
FROM '/docker-entrypoint-initdb.d/units.csv'
DELIMITER ','
CSV HEADER;

COPY public.vat(vat,vat_title)
FROM '/docker-entrypoint-initdb.d/vat.csv'
DELIMITER ','
CSV HEADER;


COPY public.auth_permission
FROM '/docker-entrypoint-initdb.d/auth_permission.csv'
DELIMITER ','
CSV HEADER;

COPY public.template_types
FROM '/docker-entrypoint-initdb.d/template_types.csv'
DELIMITER ','
CSV HEADER;