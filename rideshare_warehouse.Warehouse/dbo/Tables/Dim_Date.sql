CREATE TABLE [dbo].[Dim_Date] (
    [DateKey]       INT          NOT NULL,
    [FullDate]      DATE         NOT NULL,
    [Year]          INT          NOT NULL,
    [Quarter]       INT          NOT NULL,
    [MonthNumber]   INT          NOT NULL,
    [MonthName]     VARCHAR (20) NOT NULL,
    [DayOfMonth]    INT          NOT NULL,
    [DayOfWeekName] VARCHAR (20) NOT NULL,
    [IsWeekend]     BIT          NOT NULL,
    [HolidayFlag]   BIT          NOT NULL
);


GO