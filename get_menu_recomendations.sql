CREATE procedure [order]
                @MenuID INT
as
begin
	SET NOCOUNT ON;
	DECLARE @FreqOrderedJSON varchar(max)

SELECT @FreqOrderedJSON =(
SELECT
    RM.FoodName,
    RM.OriginalPrice,
    RM.SpecialPrice,

    (
        SELECT FFO.frequentlyorderd
        FROM Food_Frequently_Ordered AS FFO
        WHERE FFO.FoodNameID = RM.MenuID
        FOR JSON PATH
    ) AS FrequentlyOrdered,

    (
        SELECT FYMOL.youmayalsolike
        FROM Food_you_may_also_like AS FYMOL
        WHERE FYMOL.FoodNameID = RM.MenuID
        FOR JSON PATH
    ) AS YouMayAlsoLike

FROM RestaurantMenu AS RM
WHERE RM.MenuID = @MenuID
FOR JSON PATH
)

select @FreqOrderedJSON
end;
