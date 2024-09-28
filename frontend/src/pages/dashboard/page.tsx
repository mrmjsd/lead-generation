import PieChartDonut from "@/components/charts/PieChartDonut";
import ExpensesCard from "@/components/expenses-card"
import ListOfTransaction from "@/components/ListOfTransaction"
import { useGetAllAnalysis } from "@/services"

const DashboardPage = () => {

  const { data: voucherAnalysedData, isLoading } = useGetAllAnalysis();
  if (isLoading) {
    return null
  }


  return (
    <div className="space-y-4">
      <h1 className="font-semibold text-3xl">Project Expenses Tracking Software</h1>
      <div className="flex flex-wrap gap-10">
        <ExpensesCard
          expenseName="Payment Due"
          price={voucherAnalysedData.payment_dues}
        />
        <ExpensesCard
          expenseName="Inflow"
          price={voucherAnalysedData.cash_flow.Inflow}
          className="bg-pink-200"
        />
        <ExpensesCard
          expenseName="Total Outflow"
          price={voucherAnalysedData.cash_flow.Outflow}
          className="bg-green-200"
        />
      </div>
      <ListOfTransaction
        item_details={voucherAnalysedData?.item_details}
      />
      <PieChartDonut
        chartData={voucherAnalysedData.expense_categories}
      />

    </div>
  )
}

export default DashboardPage