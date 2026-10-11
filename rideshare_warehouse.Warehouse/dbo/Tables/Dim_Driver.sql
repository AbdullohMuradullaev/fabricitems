CREATE TABLE [dbo].[Dim_Driver] (
    [DriverKey]    INT            NOT NULL,
    [DriverID]     VARCHAR (50)   NOT NULL,
    [DriverName]   VARCHAR (100)  NOT NULL,
    [VehicleMake]  VARCHAR (50)   NOT NULL,
    [VehicleModel] VARCHAR (50)   NOT NULL,
    [DriverRating] DECIMAL (3, 2) NOT NULL,
    [IsActive]     BIT            NOT NULL
);


GO