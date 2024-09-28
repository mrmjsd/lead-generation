import { cn } from "@/lib/utils"

type ExpensesCard = {
    expenseName: string
    price: string,
    className?: string
}
const ExpensesCard = ({ expenseName, price,className }: ExpensesCard) => {
    return (
        <div className={cn('w-60 px-2 py-8 flex flex-col pl-7 gap-4 bg-blue-400 text-gray-700 rounded-lg',className)}>
            <h2 className="font-semibold text-lg">{expenseName}</h2>
            <p className="font-semibold leading-10 text-2xl">{`₹ ${price}`}</p>
        </div>
    )
}

export default ExpensesCard