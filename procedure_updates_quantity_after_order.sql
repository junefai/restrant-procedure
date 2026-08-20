create procedure [placed_order]
                  @FoodName varchar(100),
                  @quantity int                 
as
begin
	select FoodName,@quantity,SpecialPrice
    from RestaurantMenu
    where FoodName = @FoodName and @quantity<=MaximumItemsPerOrder;

    update RestaurantMenu 
    set quantity =quantity-@quantity
    where FoodName = @FoodName;
end;
