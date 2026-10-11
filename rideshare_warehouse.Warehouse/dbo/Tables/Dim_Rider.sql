CREATE TABLE [dbo].[Dim_Rider] (
    [RiderKey]      INT           NOT NULL,
    [RiderID]       VARCHAR (50)  NOT NULL,
    [RiderName]     VARCHAR (100) NOT NULL,
    [Email]         VARCHAR (150) NOT NULL,
    [LoyaltyTier]   VARCHAR (50)  NOT NULL,
    [EffectiveFrom] DATE          NOT NULL,
    [EffectiveTo]   DATE          NOT NULL,
    [IsCurrent]     BIT           NOT NULL
);


GO