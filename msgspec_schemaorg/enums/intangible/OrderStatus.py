import enum
from typing import ClassVar, Dict, Any

class OrderStatus(str, enum.Enum):
    """Schema.org enumeration values for OrderStatus."""

    OrderCancelled = "OrderCancelled"  # "OrderStatus representing cancellation of an order."
    OrderDelivered = "OrderDelivered"  # "OrderStatus representing successful delivery of an order."
    OrderInTransit = "OrderInTransit"  # "OrderStatus representing that an order is in transit."
    OrderPaymentDue = "OrderPaymentDue"  # "OrderStatus representing that payment is due on an order."
    OrderPickupAvailable = "OrderPickupAvailable"  # "OrderStatus representing availability of an order for pic..."
    OrderProblem = "OrderProblem"  # "OrderStatus representing that there is a problem with the..."
    OrderProcessing = "OrderProcessing"  # "OrderStatus representing that an order is being processed."
    OrderReturned = "OrderReturned"  # "OrderStatus representing that an order has been returned."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "OrderCancelled": {
            "id": "schema:OrderCancelled",
            "comment": """OrderStatus representing cancellation of an order.""",
            "label": "OrderCancelled",
        },
        "OrderDelivered": {
            "id": "schema:OrderDelivered",
            "comment": """OrderStatus representing successful delivery of an order.""",
            "label": "OrderDelivered",
        },
        "OrderInTransit": {
            "id": "schema:OrderInTransit",
            "comment": """OrderStatus representing that an order is in transit.""",
            "label": "OrderInTransit",
        },
        "OrderPaymentDue": {
            "id": "schema:OrderPaymentDue",
            "comment": """OrderStatus representing that payment is due on an order.""",
            "label": "OrderPaymentDue",
        },
        "OrderPickupAvailable": {
            "id": "schema:OrderPickupAvailable",
            "comment": """OrderStatus representing availability of an order for pickup.""",
            "label": "OrderPickupAvailable",
        },
        "OrderProblem": {
            "id": "schema:OrderProblem",
            "comment": """OrderStatus representing that there is a problem with the order.""",
            "label": "OrderProblem",
        },
        "OrderProcessing": {
            "id": "schema:OrderProcessing",
            "comment": """OrderStatus representing that an order is being processed.""",
            "label": "OrderProcessing",
        },
        "OrderReturned": {
            "id": "schema:OrderReturned",
            "comment": """OrderStatus representing that an order has been returned.""",
            "label": "OrderReturned",
        },
    }