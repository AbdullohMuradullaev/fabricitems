CREATE TABLE [dbo].[Dim_Location] (
    [LocationKey]      INT           NOT NULL,
    [CityName]         VARCHAR (100) NOT NULL,
    [StateProvince]    VARCHAR (50)  NOT NULL,
    [PostalCode]       VARCHAR (20)  NOT NULL,
    [ZoneNeighborhood] VARCHAR (100) NOT NULL
);


GO