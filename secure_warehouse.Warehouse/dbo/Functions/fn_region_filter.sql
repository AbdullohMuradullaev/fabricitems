-- Step 3: Create dynamic security predicate using mapping table
CREATE FUNCTION dbo.fn_region_filter(@region VARCHAR(50))
RETURNS TABLE
WITH SCHEMABINDING
AS
RETURN SELECT 1 AS result
WHERE EXISTS (
    SELECT 1 FROM dbo.emp_region_map m
    WHERE m.user_email = USER_NAME()
      AND m.region = @region
) OR USER_NAME() = 'tim.muradullayev@diservicesinc.com';

GO