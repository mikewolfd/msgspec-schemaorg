import enum
from typing import ClassVar, Dict, Any

class USNonprofitType(str, enum.Enum):
    """Schema.org enumeration values for USNonprofitType."""

    Nonprofit501a = "Nonprofit501a"  # "Nonprofit501a: Non-profit type referring to Farmers’ Coop..."
    Nonprofit501c1 = "Nonprofit501c1"  # "Nonprofit501c1: Non-profit type referring to Corporations..."
    Nonprofit501c10 = "Nonprofit501c10"  # "Nonprofit501c10: Non-profit type referring to Domestic Fr..."
    Nonprofit501c11 = "Nonprofit501c11"  # "Nonprofit501c11: Non-profit type referring to Teachers' R..."
    Nonprofit501c12 = "Nonprofit501c12"  # "Nonprofit501c12: Non-profit type referring to Benevolent ..."
    Nonprofit501c13 = "Nonprofit501c13"  # "Nonprofit501c13: Non-profit type referring to Cemetery Co..."
    Nonprofit501c14 = "Nonprofit501c14"  # "Nonprofit501c14: Non-profit type referring to State-Chart..."
    Nonprofit501c15 = "Nonprofit501c15"  # "Nonprofit501c15: Non-profit type referring to Mutual Insu..."
    Nonprofit501c16 = "Nonprofit501c16"  # "Nonprofit501c16: Non-profit type referring to Cooperative..."
    Nonprofit501c17 = "Nonprofit501c17"  # "Nonprofit501c17: Non-profit type referring to Supplementa..."
    Nonprofit501c18 = "Nonprofit501c18"  # "Nonprofit501c18: Non-profit type referring to Employee Fu..."
    Nonprofit501c19 = "Nonprofit501c19"  # "Nonprofit501c19: Non-profit type referring to Post or Org..."
    Nonprofit501c2 = "Nonprofit501c2"  # "Nonprofit501c2: Non-profit type referring to Title-holdin..."
    Nonprofit501c20 = "Nonprofit501c20"  # "Nonprofit501c20: Non-profit type referring to Group Legal..."
    Nonprofit501c21 = "Nonprofit501c21"  # "Nonprofit501c21: Non-profit type referring to Black Lung ..."
    Nonprofit501c22 = "Nonprofit501c22"  # "Nonprofit501c22: Non-profit type referring to Withdrawal ..."
    Nonprofit501c23 = "Nonprofit501c23"  # "Nonprofit501c23: Non-profit type referring to Veterans Or..."
    Nonprofit501c24 = "Nonprofit501c24"  # "Nonprofit501c24: Non-profit type referring to Section 404..."
    Nonprofit501c25 = "Nonprofit501c25"  # "Nonprofit501c25: Non-profit type referring to Real Proper..."
    Nonprofit501c26 = "Nonprofit501c26"  # "Nonprofit501c26: Non-profit type referring to State-Spons..."
    Nonprofit501c27 = "Nonprofit501c27"  # "Nonprofit501c27: Non-profit type referring to State-Spons..."
    Nonprofit501c28 = "Nonprofit501c28"  # "Nonprofit501c28: Non-profit type referring to National Ra..."
    Nonprofit501c3 = "Nonprofit501c3"  # "Nonprofit501c3: Non-profit type referring to Religious, E..."
    Nonprofit501c4 = "Nonprofit501c4"  # "Nonprofit501c4: Non-profit type referring to Civic League..."
    Nonprofit501c5 = "Nonprofit501c5"  # "Nonprofit501c5: Non-profit type referring to Labor, Agric..."
    Nonprofit501c6 = "Nonprofit501c6"  # "Nonprofit501c6: Non-profit type referring to Business Lea..."
    Nonprofit501c7 = "Nonprofit501c7"  # "Nonprofit501c7: Non-profit type referring to Social and R..."
    Nonprofit501c8 = "Nonprofit501c8"  # "Nonprofit501c8: Non-profit type referring to Fraternal Be..."
    Nonprofit501c9 = "Nonprofit501c9"  # "Nonprofit501c9: Non-profit type referring to Voluntary Em..."
    Nonprofit501d = "Nonprofit501d"  # "Nonprofit501d: Non-profit type referring to Religious and..."
    Nonprofit501e = "Nonprofit501e"  # "Nonprofit501e: Non-profit type referring to Cooperative H..."
    Nonprofit501f = "Nonprofit501f"  # "Nonprofit501f: Non-profit type referring to Cooperative S..."
    Nonprofit501k = "Nonprofit501k"  # "Nonprofit501k: Non-profit type referring to Child Care Or..."
    Nonprofit501n = "Nonprofit501n"  # "Nonprofit501n: Non-profit type referring to Charitable Ri..."
    Nonprofit501q = "Nonprofit501q"  # "Nonprofit501q: Non-profit type referring to Credit Counse..."
    Nonprofit527 = "Nonprofit527"  # "Nonprofit527: Non-profit type referring to political orga..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "Nonprofit501a": {
            "id": "schema:Nonprofit501a",
            "comment": """Nonprofit501a: Non-profit type referring to Farmers’ Cooperative Associations.""",
            "label": "Nonprofit501a",
        },
        "Nonprofit501c1": {
            "id": "schema:Nonprofit501c1",
            "comment": """Nonprofit501c1: Non-profit type referring to Corporations Organized Under Act of Congress, including Federal Credit Unions and National Farm Loan Associations.""",
            "label": "Nonprofit501c1",
        },
        "Nonprofit501c10": {
            "id": "schema:Nonprofit501c10",
            "comment": """Nonprofit501c10: Non-profit type referring to Domestic Fraternal Societies and Associations.""",
            "label": "Nonprofit501c10",
        },
        "Nonprofit501c11": {
            "id": "schema:Nonprofit501c11",
            "comment": """Nonprofit501c11: Non-profit type referring to Teachers' Retirement Fund Associations.""",
            "label": "Nonprofit501c11",
        },
        "Nonprofit501c12": {
            "id": "schema:Nonprofit501c12",
            "comment": """Nonprofit501c12: Non-profit type referring to Benevolent Life Insurance Associations, Mutual Ditch or Irrigation Companies, Mutual or Cooperative Telephone Companies.""",
            "label": "Nonprofit501c12",
        },
        "Nonprofit501c13": {
            "id": "schema:Nonprofit501c13",
            "comment": """Nonprofit501c13: Non-profit type referring to Cemetery Companies.""",
            "label": "Nonprofit501c13",
        },
        "Nonprofit501c14": {
            "id": "schema:Nonprofit501c14",
            "comment": """Nonprofit501c14: Non-profit type referring to State-Chartered Credit Unions, Mutual Reserve Funds.""",
            "label": "Nonprofit501c14",
        },
        "Nonprofit501c15": {
            "id": "schema:Nonprofit501c15",
            "comment": """Nonprofit501c15: Non-profit type referring to Mutual Insurance Companies or Associations.""",
            "label": "Nonprofit501c15",
        },
        "Nonprofit501c16": {
            "id": "schema:Nonprofit501c16",
            "comment": """Nonprofit501c16: Non-profit type referring to Cooperative Organizations to Finance Crop Operations.""",
            "label": "Nonprofit501c16",
        },
        "Nonprofit501c17": {
            "id": "schema:Nonprofit501c17",
            "comment": """Nonprofit501c17: Non-profit type referring to Supplemental Unemployment Benefit Trusts.""",
            "label": "Nonprofit501c17",
        },
        "Nonprofit501c18": {
            "id": "schema:Nonprofit501c18",
            "comment": """Nonprofit501c18: Non-profit type referring to Employee Funded Pension Trust (created before 25 June 1959).""",
            "label": "Nonprofit501c18",
        },
        "Nonprofit501c19": {
            "id": "schema:Nonprofit501c19",
            "comment": """Nonprofit501c19: Non-profit type referring to Post or Organization of Past or Present Members of the Armed Forces.""",
            "label": "Nonprofit501c19",
        },
        "Nonprofit501c2": {
            "id": "schema:Nonprofit501c2",
            "comment": """Nonprofit501c2: Non-profit type referring to Title-holding Corporations for Exempt Organizations.""",
            "label": "Nonprofit501c2",
        },
        "Nonprofit501c20": {
            "id": "schema:Nonprofit501c20",
            "comment": """Nonprofit501c20: Non-profit type referring to Group Legal Services Plan Organizations.""",
            "label": "Nonprofit501c20",
        },
        "Nonprofit501c21": {
            "id": "schema:Nonprofit501c21",
            "comment": """Nonprofit501c21: Non-profit type referring to Black Lung Benefit Trusts.""",
            "label": "Nonprofit501c21",
        },
        "Nonprofit501c22": {
            "id": "schema:Nonprofit501c22",
            "comment": """Nonprofit501c22: Non-profit type referring to Withdrawal Liability Payment Funds.""",
            "label": "Nonprofit501c22",
        },
        "Nonprofit501c23": {
            "id": "schema:Nonprofit501c23",
            "comment": """Nonprofit501c23: Non-profit type referring to Veterans Organizations.""",
            "label": "Nonprofit501c23",
        },
        "Nonprofit501c24": {
            "id": "schema:Nonprofit501c24",
            "comment": """Nonprofit501c24: Non-profit type referring to Section 4049 ERISA Trusts.""",
            "label": "Nonprofit501c24",
        },
        "Nonprofit501c25": {
            "id": "schema:Nonprofit501c25",
            "comment": """Nonprofit501c25: Non-profit type referring to Real Property Title-Holding Corporations or Trusts with Multiple Parents.""",
            "label": "Nonprofit501c25",
        },
        "Nonprofit501c26": {
            "id": "schema:Nonprofit501c26",
            "comment": """Nonprofit501c26: Non-profit type referring to State-Sponsored Organizations Providing Health Coverage for High-Risk Individuals.""",
            "label": "Nonprofit501c26",
        },
        "Nonprofit501c27": {
            "id": "schema:Nonprofit501c27",
            "comment": """Nonprofit501c27: Non-profit type referring to State-Sponsored Workers' Compensation Reinsurance Organizations.""",
            "label": "Nonprofit501c27",
        },
        "Nonprofit501c28": {
            "id": "schema:Nonprofit501c28",
            "comment": """Nonprofit501c28: Non-profit type referring to National Railroad Retirement Investment Trusts.""",
            "label": "Nonprofit501c28",
        },
        "Nonprofit501c3": {
            "id": "schema:Nonprofit501c3",
            "comment": """Nonprofit501c3: Non-profit type referring to Religious, Educational, Charitable, Scientific, Literary, Testing for Public Safety, Fostering National or International Amateur Sports Competition, or Prevention of Cruelty to Children or Animals Organizations.""",
            "label": "Nonprofit501c3",
        },
        "Nonprofit501c4": {
            "id": "schema:Nonprofit501c4",
            "comment": """Nonprofit501c4: Non-profit type referring to Civic Leagues, Social Welfare Organizations, and Local Associations of Employees.""",
            "label": "Nonprofit501c4",
        },
        "Nonprofit501c5": {
            "id": "schema:Nonprofit501c5",
            "comment": """Nonprofit501c5: Non-profit type referring to Labor, Agricultural and Horticultural Organizations.""",
            "label": "Nonprofit501c5",
        },
        "Nonprofit501c6": {
            "id": "schema:Nonprofit501c6",
            "comment": """Nonprofit501c6: Non-profit type referring to Business Leagues, Chambers of Commerce, Real Estate Boards.""",
            "label": "Nonprofit501c6",
        },
        "Nonprofit501c7": {
            "id": "schema:Nonprofit501c7",
            "comment": """Nonprofit501c7: Non-profit type referring to Social and Recreational Clubs.""",
            "label": "Nonprofit501c7",
        },
        "Nonprofit501c8": {
            "id": "schema:Nonprofit501c8",
            "comment": """Nonprofit501c8: Non-profit type referring to Fraternal Beneficiary Societies and Associations.""",
            "label": "Nonprofit501c8",
        },
        "Nonprofit501c9": {
            "id": "schema:Nonprofit501c9",
            "comment": """Nonprofit501c9: Non-profit type referring to Voluntary Employee Beneficiary Associations.""",
            "label": "Nonprofit501c9",
        },
        "Nonprofit501d": {
            "id": "schema:Nonprofit501d",
            "comment": """Nonprofit501d: Non-profit type referring to Religious and Apostolic Associations.""",
            "label": "Nonprofit501d",
        },
        "Nonprofit501e": {
            "id": "schema:Nonprofit501e",
            "comment": """Nonprofit501e: Non-profit type referring to Cooperative Hospital Service Organizations.""",
            "label": "Nonprofit501e",
        },
        "Nonprofit501f": {
            "id": "schema:Nonprofit501f",
            "comment": """Nonprofit501f: Non-profit type referring to Cooperative Service Organizations.""",
            "label": "Nonprofit501f",
        },
        "Nonprofit501k": {
            "id": "schema:Nonprofit501k",
            "comment": """Nonprofit501k: Non-profit type referring to Child Care Organizations.""",
            "label": "Nonprofit501k",
        },
        "Nonprofit501n": {
            "id": "schema:Nonprofit501n",
            "comment": """Nonprofit501n: Non-profit type referring to Charitable Risk Pools.""",
            "label": "Nonprofit501n",
        },
        "Nonprofit501q": {
            "id": "schema:Nonprofit501q",
            "comment": """Nonprofit501q: Non-profit type referring to Credit Counseling Organizations.""",
            "label": "Nonprofit501q",
        },
        "Nonprofit527": {
            "id": "schema:Nonprofit527",
            "comment": """Nonprofit527: Non-profit type referring to political organizations.""",
            "label": "Nonprofit527",
        },
    }