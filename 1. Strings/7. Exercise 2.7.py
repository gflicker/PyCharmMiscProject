# Removing whitespaces or stripping
name_with_spaces = "   Caramel Princessa "
print(f"\t{name_with_spaces},\n\twill you marry me?")

#Stripped whitespaces
print(f"\t{name_with_spaces.rstrip()},\n\twill you marry me?")
#left strip
print(f"\t{name_with_spaces.lstrip()},\n\twill you marry me?")
#strip both left and right
print(f"\t{name_with_spaces.strip()},\n\twill you marry me?")