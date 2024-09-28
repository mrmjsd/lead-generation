import DashboardLayout from '@/layouts/DashboardLayout';
import DashboardPage from '@/pages/dashboard/page';
import TransactionPage from '@/pages/transactions/page';
import { RouterProvider, createBrowserRouter } from "react-router-dom";

const Routes = () => {
    const router = createBrowserRouter([
        {
            path: '',
            element: <DashboardLayout />,
            children: [
                { path: 'dashboard', element: <DashboardPage /> },
                { path: 'transactions', element: <TransactionPage /> },
            ]
        },
    ]);

    return <RouterProvider router={router} />;
};

export default Routes;
