class CategoryAnalysisService:

    def analyze(
        self,
        report
    ):

        if not report["categories"]:

            return None

        top_category = max(
            report["categories"],
            key=lambda category:
            sum(
                item["amount"]
                for item in report["categories"][
                    category
                ]
            )
        )

        total = sum(
            item["amount"]
            for item in report["categories"][
                top_category
            ]
        )

        return {
            "top_category": top_category,
            "amount": total
        }