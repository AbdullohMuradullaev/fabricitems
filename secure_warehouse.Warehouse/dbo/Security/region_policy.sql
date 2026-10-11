CREATE SECURITY POLICY [dbo].[region_policy]
    ADD FILTER PREDICATE [dbo].[fn_region_filter]([region]) ON [dbo].[employees]
    WITH (STATE = ON);


GO