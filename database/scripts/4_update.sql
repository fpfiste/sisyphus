
/********************************/
/*********** UPDATE 2.0 *********/
/********************************/

do
$do$
declare div_revenue_id int;
begin



CREATE TABLE if not exists public.revenue_type (
	id_revenue_type serial NOT NULL,
	revenue_type varchar(30) NOT NULL,
	pl_account_number varchar(20),
	CONSTRAINT revenue_type_pk PRIMARY KEY (id_revenue_type)
);

IF not EXISTS ( SELECT 1 FROM public.revenue_type WHERE revenue_type = 'Diverser Umsatz' )
then
    INSERT INTO public.revenue_type (revenue_type)
    VALUES('Diverser Umsatz');
end if;

select rt.id_revenue_type into div_revenue_id from public.revenue_type rt where revenue_type = 'Diverser Umsatz';


alter table public.sales
add column if not exists fk_revenue_type int REFERENCES public.revenue_type(id_revenue_type),
add column if not exists invoice_position_nr int;

alter table public.companies
add column if not exists invoice_receiver varchar(200);

alter table public.tasks
add column if not exists fk_revenue_type int REFERENCES public.revenue_type(id_revenue_type),
add column if not exists invoice_position_nr int;

alter table public.templates
add column if not exists fk_revenue_type int REFERENCES public.revenue_type(id_revenue_type);



alter table public.sales
add column if not exists changed_on timestamp,
add column if not exists changed_by varchar(200),
add column if not exists history jsonb DEFAULT '{}'::jsonb NULL;

alter table public.tasks
add column if not exists changed_on timestamp ,
add column if not exists changed_by varchar(200),
add column if not exists history jsonb DEFAULT '{}'::jsonb NULL;

update public.sales
set fk_revenue_type = @div_revenue_id
where fk_revenue_type is null;

update public.tasks
set fk_revenue_type = @div_revenue_id
where fk_revenue_type is null;


end
$do$