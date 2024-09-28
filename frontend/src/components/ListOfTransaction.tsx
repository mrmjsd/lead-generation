type ItemDetails = {
    description: string
    amount: number
    voucher_no: string
    employee: {
        name: string
        code: string
    }
}

const ListOfTransaction = ({ item_details }: { item_details: ItemDetails[] }) => {
    return (
        <div className="flex flex-col gap-4 h-[50vh] overflow-auto">
            <table className="w-1/2 border bg-slate-200 rounded">
                <thead>
                    <tr className="h-12">
                        <th className="border">Employee Name</th>
                        <th>Amount</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        item_details?.length === 0 &&
                        <tr>
                            <td colSpan={5} className='text-center'>No Details</td>
                        </tr>
                    }
                    {
                        item_details?.map(({ amount, description, employee }, index) => {
                            return (
                                <tr key={index} className="my-4">
                                    <td className="px-4">
                                        <div>
                                            <h4>{employee?.name ==='N/A'?description:employee?.name}</h4>
                                        </div>
                                    </td>
                                    <td>{amount} %</td>
                                </tr>
                            )
                        }
                        )
                    }
                </tbody>
            </table>
        </div>
    )
}

export default ListOfTransaction