CREATE TABLE [dbo].[Dim_Trip_Type] (
    [TripTypeKey]     INT          NOT NULL,
    [TripTypeName]    VARCHAR (50) NOT NULL,
    [ServiceCategory] VARCHAR (50) NOT NULL,
    [IsSharedRide]    BIT          NOT NULL
);


GO