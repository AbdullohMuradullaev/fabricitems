CREATE TABLE [dbo].[employees] (
    [emp_id]         INT                                                              NULL,
    [name]           VARCHAR (100)                                                    NULL,
    [department]     VARCHAR (50)                                                     NULL,
    [region]         VARCHAR (50)                                                     NULL,
    [salary]         DECIMAL (10, 2) MASKED WITH (FUNCTION = 'default()')             NULL,
    [ssn]            VARCHAR (20) MASKED WITH (FUNCTION = 'partial(0, "XXX-XX-", 4)') NULL,
    [email]          VARCHAR (100) MASKED WITH (FUNCTION = 'email()')                 NULL,
    [manager_region] VARCHAR (50)                                                     NULL
);


GO