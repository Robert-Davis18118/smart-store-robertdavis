-- Customers Dimension Table
CREATE TABLE dim_customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    LoyaltyPoints INT,
    CustomerSegment VARCHAR(50)
);
-- Sales Fact Table
CREATE TABLE fact_sales (
    TransactionID INT PRIMARY KEY,
    SaleDate DATE,
    CustomerID INT,
    ProductID INT,
    StoreID INT,
    CampaignID INT,
    SaleAmount DECIMAL(10, 2),
    DiscountPercent DECIMAL(5, 2),
    PaymentType VARCHAR(20),
    FOREIGN KEY (CustomerID) REFERENCES dim_customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES dim_products(ProductID)
);
