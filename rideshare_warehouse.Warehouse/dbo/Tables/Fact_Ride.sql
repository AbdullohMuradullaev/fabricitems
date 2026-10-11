CREATE TABLE [dbo].[Fact_Ride] (
    [RideID]               BIGINT          NOT NULL,
    [DateKey]              INT             NOT NULL,
    [PickupLocationKey]    INT             NOT NULL,
    [DropoffLocationKey]   INT             NOT NULL,
    [TripTypeKey]          INT             NOT NULL,
    [DriverKey]            INT             NOT NULL,
    [RiderKey]             INT             NOT NULL,
    [TripDistanceMiles]    DECIMAL (8, 2)  NOT NULL,
    [TripDurationSeconds]  INT             NOT NULL,
    [BaseFareAmount]       DECIMAL (10, 2) NOT NULL,
    [SurgeMultiplier]      DECIMAL (4, 2)  NOT NULL,
    [TipAmount]            DECIMAL (10, 2) NOT NULL,
    [TotalFareAmount]      DECIMAL (10, 2) NOT NULL,
    [DriverEarningsAmount] DECIMAL (10, 2) NOT NULL
);


GO